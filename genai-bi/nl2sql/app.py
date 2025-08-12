from fastapi import FastAPI
from pydantic import BaseModel
from sqlglot import parse_one, exp
import os, requests, psycopg2

OAI_BASE = os.environ.get("OAI_BASE","http://ollama:11434/v1")
OAI_KEY  = os.environ.get("OAI_KEY","ollama")
MODEL    = os.environ.get("MODEL","mannix/defog-llama3-sqlcoder-8b:q5_k_s")
DB_DSN   = os.environ["DB_DSN"]  # e.g. postgresql://nl2sql:ChangeMe!@postgres:5432/analytics

SYSTEM = """You are a senior analytics engineer.
Only output a single SQL SELECT for Postgres.
Use explicit column names (never SELECT *) and return <=100 rows.
"""

class Ask(BaseModel):
    question: str
    schema_catalog: str            # whitelist from dbt (table/column names + descriptions)
    few_shots: list[dict] = []     # [{"q":"...", "sql":"..."}]

app = FastAPI()

def validate_sql(sql: str, dialect="postgres") -> str:
    node = parse_one(sql, read=dialect)
    if not isinstance(node, exp.Select):  # single SELECT only
        raise ValueError("Only a single SELECT is allowed")
    if not node.find(exp.Limit):
        node = node.limit(100)
    text = node.sql(dialect=dialect).lower()
    for bad in ("insert","update","delete","drop","alter","create","truncate"):
        if bad in text:
            raise ValueError("Non-SELECT keyword detected")
    return node.sql(dialect=dialect)

@app.post("/sql")
def nl2sql(req: Ask):
    msgs = [
        {"role":"system","content": SYSTEM + "\nSchema:\n" + req.schema_catalog},
        {"role":"user","content": req.question},
    ]
    for s in req.few_shots:
        msgs += [{"role":"user","content": s["q"]},
                 {"role":"assistant","content": s["sql"]}]

    r = requests.post(f"{OAI_BASE}/chat/completions",
                      headers={"Authorization": f"Bearer {OAI_KEY}"},
                      json={"model": MODEL, "messages": msgs, "temperature": 0.1, "max_tokens": 512})
    r.raise_for_status()
    raw = r.json()["choices"][0]["message"]["content"].strip().strip("`")
    sql = validate_sql(raw)

    with psycopg2.connect(DB_DSN) as conn, conn.cursor() as cur:
        cur.execute("SET statement_timeout = '10s'")
        cur.execute(sql)
        rows = cur.fetchall()
        cols = [d.name for d in cur.description]
    return {"sql": sql, "columns": cols, "rows": rows}
