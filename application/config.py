# An interface for configuration file but we shall maintain instance of the database that configuration points to.
# For this, we shall provide a method that will call __init__()

from typing import Dict, Any
from database.database import Database
from database import spinup_db_instance


class AppConfig:

    def __init__(self, conf: Dict[str, Any], db_instance: Database):
        self.conf = conf
        self.db_instance = db_instance

    @classmethod
    def parse_config(cls, raw: dict):
        conf = raw.copy()
        db_instance = spinup_db_instance(conf['Database'])
        return cls(conf, db_instance)
