# Starting point of Application which is called as:
#        app.sh --> app.py --> app_cli.py
#        app.py --> app_cli.py

import json
from typing import List
from application.app_parser import parse_args
from application.config import AppConfig


def run(argv: List[str]):
    print("starting app_cli.run() now.........")
    # Get passed arguments first
    args = parse_args(argv)

    print(f"Welcome {args.name}")

    # Load json configuration file to dictionary
    with open(args.config_file) as config_file:
        conf_dict = json.load(config_file)

    # Parse the configuration dictionary and spin up db_instance
    conf = AppConfig.parse_config(conf_dict)

    # Check whether we have spin up correct Database
    print(conf.db_instance)
    print(conf.db_instance.get_table_names(type="table"))

