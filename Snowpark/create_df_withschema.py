from snowflake.snowpark import Session

from snowflake.snowpark.types import IntegerType, StructField, StructType, DateType

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
session.sql("use warehouse compute_wh").collect()

schema = StructType([StructField("one", IntegerType()),
StructField("two",  IntegerType()),
StructField("three",  IntegerType()),
StructField("four",  DateType())])

test = session.create_dataframe([[1, 2, 3, '2022-01-26'],[1, 2, 3, '2022-01-26'],[1, 2, 3, '2022-01-26'],[1, 2, 3, '2022-01-26']], schema=["a","b","c","d"])
test.show()

test = session.create_dataframe([[1, 2, 3, '2022-01-26'],[1, 2, 3, '2022-01-26'],[1, 2, 3, '2022-01-26'],[1, 2, 3, '2022-01-26']], schema=schema)
test.show()