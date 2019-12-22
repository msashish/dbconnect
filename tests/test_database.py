import unittest
from tests.test_utility import sqlite_config
from application.config import AppConfig
from application.database.sqlite_database import SQLiteDatabase
from pathlib import Path


class TestDatabaseAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.cfg = sqlite_config()

    def test_database(self):
        conf = AppConfig.get_enhanced_config(self.cfg)
        # If you want to run this test class using Run then below should be uncommented.
        # conf.db_instance.run_scripts(Path("/Users/sheelava/Documents/main/github/dbconnect/sql/sqlite_ddl.sql"))
        list_of_tables = conf.db_instance.get_table_names(type="table")
        self.assertIsInstance(conf.db_instance, SQLiteDatabase)
        self.assertEqual(3, len(list_of_tables))
        self.assertEqual('CUSTOMER', list_of_tables[0]['TBL_NAME'])
