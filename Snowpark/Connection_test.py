import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

connection_parameters = {"account":"MBB19684",
"user":"SIVANAND1993",
"password": "Pass@tensor2378",
"role":"ACCOUNTADMIN",
"warehouse":"COMPUTE_WH",
"database":"SNOWFLAKE_SAMPLE_DATA",
"schema":"TPCDS_SF100TCL"
}

test_session = Session.builder.configs(connection_parameters).create()

print(test_session.sql("select current_warehouse(), current_database(), current_schema()").collect())

session = Session.builder.configs(connection_parameters).create()