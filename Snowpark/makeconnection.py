import sys
from snowflake.snowpark import Session
sys.path.append('/Users/pradeep/Downloads/Udemy_course_videos/course_2_assignments/Snowpark_pipeline/')
from generic_code import code_library

# Make connection and create Snowpark session
connection_parameters = {"account":"rh80922.ap-southeast-1", \
"user":"pradeep", \
"password": "*****", \
"role":"ACCOUNTADMIN", \
"warehouse":"COMPUTE_WH", \
"database":"DEMO_DB", \
"schema":"PUBLIC" \
}

session_new = code_library.snowconnection(connection_parameters)


session = snowconnection(connection_parameters)



put file:///Users/pradeep/Downloads/scrub/scrubadub/scrubbers.py @DEMO_DB.PUBLIC.UDF_STAGE/scrubadub/;