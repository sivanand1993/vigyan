import json, pathlib

manifest = pathlib.Path("target/manifest.json")
out = pathlib.Path("schema_catalog.txt")

if not manifest.exists():
    raise SystemExit("manifest.json not found. Run: dbt run && dbt compile first.")

m = json.loads(manifest.read_text(encoding="utf-8"))
whitelist = []

for node in m["nodes"].values():
    if node.get("resource_type") == "model" and "exposed_to_ai" in node.get("tags", []):
        db, sch, nm = node["database"], node["schema"], node["name"]
        cols = node.get("columns", {})
        col_lines = [f"  {c} -- {cols[c].get('description','')}" for c in cols]
        whitelist.append(f"{db}.{sch}.{nm}(\n" + "\n".join(col_lines) + "\n)")

out.write_text("\n\n".join(whitelist), encoding="utf-8")
print(f"Wrote {out.resolve()}")
