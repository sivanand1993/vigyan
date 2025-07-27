import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import IntegerType, StructField, StructType, DateType, StringType

# Replace the below connection_parameters with your respective snowflake account,user name and password

connection_parameters = {"account":"MBB19684",
"user":"SIVANAND1993",
"password": "Pass@tensor2378",
"role":"ACCOUNTADMIN",
"warehouse":"COMPUTE_WH",
"database":"DEMO_DB",
"schema":"PUBLIC"
}
session = Session.builder.configs(connection_parameters).create()
schema = StructType([StructField("Name", StringType()),
StructField("Salary",  IntegerType()),
StructField("Doj",  DateType())])

test = session.create_dataframe([["John", "100","2016-01-01"],["Sam", "200","2017-01-01"]], schema=["a","b"])
test.show()

test = session.sql("select O_ORDERKEY,O_ORDERSTATUS,O_TOTALPRICE from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.ORDERS")
test.describe().sort("Summary").show()