#!/usr/bin/env python3
import sys

from application import app_cli

if __name__ == "__main__":
    app_cli.run(sys.argv[1:])
