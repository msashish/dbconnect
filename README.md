# dbconnect

Spin up a database based on configuration

# Usage:

## To run directly on a Mac: 

ksh app.sh --name "Someone"

## To run anywhere python 3.6 is installed:
python3 app.py --name "SomeoneElse"

## To run using container made up of Cent Os :
cd docker

docker-compose up

# However, if you still want to manually test & coverage check 
[Better to do it in a virtual environment]

cd dbconnect

virtualenv venv

pip install --no-cache-dir -r docker/requirements.txt

source venv/bin/activate  (FOr non MacOs source is not needed)

python -m unittest discover tests

python -m coverage run --include='application/*' --branch -m unittest discover -b

deactivate