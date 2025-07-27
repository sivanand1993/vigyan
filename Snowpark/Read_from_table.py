from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
import time

from snowflake.snowpark.types import IntegerType, StringType, StructField, StructType, DateType

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

test = session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.CUSTOMER")
test.show(20)

test = session.table("DEMO_DB.PUBLIC.CUSTOMER")
type(test)
t = test.cache_result()

test = session.sql("select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.CUSTOMER WHERE C_NATIONKEY='23'")
type(test)
test.show()

test3 = test.filter(col("C_NATIONKEY")=='23').select("C_NAME","C_NATIONKEY","C_ACCTBAL")
type(test3)
test3.show()


test4 = test3.select("C_NATIONKEY","C_ACCTBAL")
test4.show()
type(test4)

test2 = test.na.drop()
test2.show()

type(test2)
