
import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

connection_parameters = {"account":"********",
"user":"*****",
"password": "*******",
"role":"ACCOUNTADMIN",
"warehouse":"COMPUTE_WH",
"database":"DEMO_DB",
"schema":"PUBLIC"
}

session = Session.builder.configs(connection_parameters).create()

print(session.sql("select current_warehouse(), current_database(), current_schema()").collect())


#1 Create a query that displays EMPFNAME, 
# EMPLNAME, DEPTCODE, DEPTNAME, LOCATION
#  from EMPLOYEE, and DEPARTMENT tables. 
# Make sure the results are in the ascending 
# order based on the EMPFNAME and LOCATION of the department.

    # SELECT E.EMPFNAME, E.EMPLNAME, E.DEPTCODE,
    #        D.DEPTNAME, D.LOCATION
    #        FROM EMPLOYEE E, DEPARTMENT D
    #        WHERE E.DEPTCODE = D.DEPTCODE
    #        ORDER BY E.EMPFNAME, D.LOCATION;

#STEP 1: Read data from EMPLOYEE and LOCATION to dataframe, emp_stg_tbl and emp_dpt_tbl



#STEP 2: Join dataframe, emp_stg_tbl and emp_dpt_tbl by column DEPTCODE and create data-frame, emp_dpt_join



#STEP3:  Select only columns, "EMPFNAME","EMPLNAME","DEPTCODE","DEPTNAME","LOCATION"  from data-frame emp_dpt_join and create data-frame by name, emp_dpt_select




#STEP4:  Mention command to order column by EMPFNAME in ascending order and create dataframe by name, emp_dpt_order_by

