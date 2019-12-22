# An interface for configuration file but we shall also add instance of the database that configuration points to.
# For this, we shall provide a method that will call __init__()

from typing import Dict, Any
from application.database.database import Database
from application.database import spinup_db_instance
import json


class AppConfig:

    def __init__(self, conf: Dict[str, Any], db_instance: Database):
        self.conf = conf
        self.db_instance = db_instance

    @classmethod
    def get_enhanced_config(cls, raw: dict):
        """
        Add appropriate database instance inti the configuration
        """
        conf = raw.copy()
        db_instance = spinup_db_instance(conf['Database'])
        # Remove any config parameters if you want del conf['Database']
        del conf['Database']
        return cls(conf, db_instance)

    @staticmethod
    def load_json(json_file) -> dict:
        with open(json_file) as config_file:
            conf_dict = json.load(config_file)
        return conf_dict
