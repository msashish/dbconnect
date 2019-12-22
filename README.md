# dbconnect

Spin up a database based on configuration

# To test & coverage check
cd dbconnect

virtualenv venv

source venv/bin/activate

python -m unittest discover tests

python -m coverage run --include='application/*' --branch -m unittest discover -b

# Usage information:

## To run on a Mac: 

ksh app.sh --name "Ashish"

## To run anywhere python 3.6 or more is installed:
python3 app.py --name "SomeoneElse"

## To run on Cent Os:
cd docker

docker-compose up