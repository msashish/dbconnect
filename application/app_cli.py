# Starting point of Application which is called as:
#        app.sh --> app.py --> app_cli.py
#        app.py --> app_cli.py

from typing import List
from application.app_parser import parse_args
from application.config import AppConfig


def run(argv: List[str]):
    print("starting application")
    # Get passed arguments first
    args = parse_args(argv)
    print(f"Welcome {args.name}")

    # Load json configuration file to dictionary
    conf_dict = AppConfig.load_json(args.config_file)

    # Parse the configuration dictionary and spin up db_instance. Enhanced config now has db_instance as well
    conf = AppConfig.get_enhanced_config(conf_dict)
    print(conf.__dict__)

    # Check whether we have spin up correct Database
    print(conf.db_instance.get_table_names(type="table"))

