import os
import cx_Oracle
from database.database import Database


class OracleDatabase(Database):
    def __init__(self, oracle_home,connect_identifier, oracle_schema, tns_admin):
        # Set Environment variable
        os.environ.putenv('ORACLE_HOME', oracle_home)
        os.environ.putenv('TNS_ADMIN', tns_admin)

        # Establish connection
        conn = cx_Oracle.connect(connect_identifier)
        super().__init__(conn)


