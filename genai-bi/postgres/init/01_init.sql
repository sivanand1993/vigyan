-- This file runs on first start, connected to DB = analytics.

-- Lightdash metadata DB
CREATE DATABASE lightdash;

-- Read-only role for BI/NL2SQL
CREATE ROLE bi_reader NOINHERIT;
GRANT CONNECT ON DATABASE analytics TO bi_reader;
GRANT USAGE ON SCHEMA public TO bi_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO bi_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO bi_reader;

-- Service user for NL→SQL
CREATE USER nl2sql WITH PASSWORD '${NL2SQL_PASSWORD}';
GRANT bi_reader TO nl2sql;

-- Safety: short timeouts (adjust as needed)
ALTER DATABASE analytics SET statement_timeout = '10s';

-- Demo table
CREATE TABLE IF NOT EXISTS public.fct_orders (
  order_id bigserial PRIMARY KEY,
  order_date date NOT NULL,
  account_id int NOT NULL,
  total_amount numeric(12,2) NOT NULL
);

INSERT INTO public.fct_orders (order_date, account_id, total_amount) VALUES
('2025-07-01',101,49.99),('2025-07-02',101,19.00),('2025-07-03',102,120.00),
('2025-08-01',101,11.50),('2025-08-02',103,300.00)
ON CONFLICT DO NOTHING;
