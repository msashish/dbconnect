import argparse, os
from typing import List


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Some Application')

    # arguments passed will be in values and they will be populated into dest variables inside __call__() method
    # of action class
    parser.add_argument('--name', dest='name',
                        required=True, help='Just your name. Its a dummy app...')
    parser.add_argument('--config', dest='config_file', default='config/config.json',
                        required=False, help='Configuration file for App',
                        action=ValidateConfigFileAction)

    return parser.parse_args(args=args)


class ValidateConfigFileAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not os.path.exists(values):
            raise argparse.ArgumentError(self, f"Config {values} does not exist.")
        if not os.path.isfile(values):
            raise argparse.ArgumentError(self, f"Config {values} is not a file.")

        setattr(namespace, self.dest, values)
