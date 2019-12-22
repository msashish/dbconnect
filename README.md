# **dbconnect**

Spin up a database based on configuration

# **Usage:**

## 1) To run directly on a Mac: 

ksh app.sh --name "Someone"

## 2) To run anywhere python 3.6 is installed:
python3 app.py --name "SomeoneElse"

## 3) To run using container made up of Cent Os :
cd docker

docker-compose up

# **However, if you still want to manually test & coverage check** 
[Better to do it in a virtual environment]

cd dbconnect

virtualenv venv

pip install --no-cache-dir -r docker/requirements.txt

source venv/bin/activate  (For non-Mac users, 'source' is not needed)

python -m unittest discover tests

python -m coverage run --include='application/*' --branch -m unittest discover -b

deactivate