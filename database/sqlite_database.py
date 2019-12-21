from database.database import Database
import sqlite3


class SQLiteDatabase(Database):

    def __init__(self, db_schema):
        conn = sqlite3.connect(db_schema)
        super().__init__(conn)

    @classmethod
    def get_db_instance(cls, schema):
        db_instance = cls(schema)
        return db_instance
