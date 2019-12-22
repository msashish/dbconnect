import unittest
from application.app_parser import parse_args
from tempfile import NamedTemporaryFile
from pathlib import Path


class TestParser(unittest.TestCase):

    def test_app_parser(self):
        args = ['test', '--name', 'Ashish']
        # args_collected = parse_args(["--name=Ashish"])
        args_collected = parse_args(args[1:])
        self.assertEqual(args_collected.name, "Ashish")
        self.assertEqual(args_collected.config_file, 'config/config.json')

    def test_parser_valid_args(self):
        name = 'Some Person'
        with NamedTemporaryFile() as temp_config:
            config_path = Path(temp_config.name).resolve()
            config_path.touch()

            parsed_args = parse_args([
                f"--name={name}",
                f"--config={config_path}",
            ])

        self.assertEqual(parsed_args.name, name)
        self.assertEqual(parsed_args.config_file, str(config_path))

    # https://docs.python.org/3.3/library/unittest.html#unittest.TestCase.assertRaises
    def test_missing_args(self):
        args = ['test']
        with self.assertRaises(SystemExit) as sys_exit:
            parse_args(args[1:])
        rc = sys_exit.exception
        self.assertEqual(rc.code, 2)
