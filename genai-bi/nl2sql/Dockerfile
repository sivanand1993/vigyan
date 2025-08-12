FROM python:3.11-slim
WORKDIR /app
COPY app.py /app/app.py
RUN pip install --no-cache-dir fastapi uvicorn sqlglot requests psycopg2-binary
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]
