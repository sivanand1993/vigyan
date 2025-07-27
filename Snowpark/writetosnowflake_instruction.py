# Execute below commands in snowflake before you start

# create database demo_db;
# use database demo_db;

# create or replace file format my_csv_s3_format
# type = csv field_delimiter = ',' skip_header = 1 null_if = ('NULL', 'null') empty_field_as_null = true FIELD_OPTIONALLY_ENCLOSED_BY='"';


# create or replace stage my_s3_stage  
#   url = 's3://snowflakesmpdata'
#   file_format = my_csv_s3_format;
  
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

from snowflake.snowpark.types import IntegerType, StringType, StructField, StructType, DateType

# Replace the below connection_parameters with your respective snowflake account,user name and password
connection_parameters = {"account":"********",
"user":"*****",
"password": "*******",
"role":"ACCOUNTADMIN",
"warehouse":"COMPUTE_WH",
"database":"DEMO_DB",
"schema":"PUBLIC"
}

session = Session.builder.configs(connection_parameters).create()


schema = StructType([StructField("FIRST_NAME", StringType()),
StructField("LAST_NAME", StringType()),
StructField("EMAIL", StringType()),
StructField("ADDRESS", StringType()),
StructField("CITY", StringType()),
 StructField("DOJ",DateType())])

# Use session.read.schema and session.read.csv and mention the command to read data from s3
employee_s3 = session.read.schema(schema).csv('@my_s3_stage/employee/employees01.csv')

# Write data frame employee_s3 to employee table in snowflake.


# read one more file from the aws s3 location.
employee_s3 = session.read.schema(schema).csv('@my_s3_stage/employee/employees02.csv')

# Append this data to employee table in snowflake