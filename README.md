# **dbconnect**

Spin up a database based on configuration. By default uses sqlite however you can configure other database (refer to /config/)

Tests for CI is done @ https://travis-ci.org/msashish/dbconnect

# App Structure

```bash
--dbconnect
      |-- .git
      |-- .travis.yml
      |-- app.sh
      |-- app.py
      |-- application
             |-- app_cli.py
             |-- config.py
             |-- app_parser.py
             |-- database
                      |-- __init__.py
                      |-- database.py
                      |-- sqlite_database.py
                      |-- oracle_database.py
      |-- config
             |-- config.json
             |-- oracle_config.json
      |-- docker
             |-- Dockerfile
             |-- docker-compose.yml
             |-- requirements.txt
             |-- run_tests.sh
      |-- tests
      |-- sql
             |-- sqlite_ddl.json
```



# **Usage:**

## 1) To run directly on a Mac: 

```bash
ksh app.sh --name "Someone"
```

## 2) To run anywhere python 3.6 is installed:

```bash
python3 app.py --name "SomeoneElse"
```

## 3) To run using container made up of Cent Os :
```bash
cd docker
docker-compose up
```

# **However, if you still want to manually test** 
[Better to do it in a virtual environment]

```bash
cd dbconnect
virtualenv venv
pip install --no-cache-dir -r docker/requirements.txt
source venv/bin/activate  (For non-Mac users, 'source' is not needed)
python -m unittest discover tests
python -m coverage run --include='application/*' --branch -m unittest discover -b
deactivate
```