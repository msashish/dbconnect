from application.database.database import Database
import sqlite3


class SQLiteDatabase(Database):

    def __init__(self, db_schema):
        conn = sqlite3.connect(db_schema)
        super().__init__(conn)

    def run_scripts(self, sql_file):
        with open(sql_file) as sql_file:
            sql_scripts = sql_file.read()
        with self.conn as conn:
            conn.executescript(sql_scripts)
