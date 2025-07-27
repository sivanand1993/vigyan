from snowflake.snowpark import Session
from snowflake.snowpark import Window
from snowflake.snowpark.functions import col,min as _min,rank,max,avg,sum as sum_
import time

from snowflake.snowpark.types import IntegerType, StringType, StructField, StructType, DateType

connection_parameters = {"account":"MBB19684",
"user":"SIVANAND1993",
"password": "Pass@tensor2378",
"role":"ACCOUNTADMIN",
"warehouse":"COMPUTE_WH",
"database":"DEMO_DB",
"schema":"PUBLIC"
}

session = Session.builder.configs(connection_parameters).create()

emp_stg_tbl=session.table("EMPLY")
emp_stg_tbl.show()

emp_dpt_tbl=session.table("DEPARTMENT")
emp_dpt_tbl.show()

emp_dpt_join=emp_stg_tbl.join(emp_dpt_tbl,emp_dpt_tbl.DEPTCODE == emp_stg_tbl.DEPTCODE,"inner")
emp_dpt_join.show()

emp_dpt_select=emp_dpt_join.select("EMPFNAME","EMPLNAME",emp_stg_tbl["DEPTCODE"],"DEPTNAME","LOCATION")
emp_dpt_select.show()

total_salary=session.table("EMPLY").group_by("EMPFNAME").agg(sum_(col("COMMISSION")+col("SALARY")).alias("TOTAL_SALARY"))
total_salary.show()