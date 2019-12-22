import unittest
from application.config import AppConfig
from application.database.sqlite_database import SQLiteDatabase
from application.database.database import Database
from tests.test_utility import sqlite_config, make_empty_dir, make_file


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.cfg = sqlite_config()
        self.dummy_test_file = 'test_files/test_config.json'
        make_empty_dir('test_files')
        make_file(self.dummy_test_file,
                  """
                  {"1": "Something", "2": {"2.1": "Inside Something", "2.2": "Inside Something Else"}}
        """)

    def test_get_enhanced_config(self):
        enhanced_config = AppConfig.get_enhanced_config(self.cfg)
        self.assertIsInstance(enhanced_config.db_instance, SQLiteDatabase)
        self.assertIsInstance(enhanced_config.db_instance, Database)

    def test_load_json(self):
        conf_dict = AppConfig.load_json(self.dummy_test_file)
        self.assertEqual(conf_dict["1"], "Something")
        self.assertEqual(conf_dict["2"]["2.2"], "Inside Something Else")
