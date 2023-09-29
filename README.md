# La-pizza
La Pizza is a Flask API that allows users to access information  about pizza restaurants.

## Table of content
* Files
* Usage
* Dependencies
* installation
* Author


## Files
1. app.py: This is the main Python file that defines the Flask application and API routes. It also contains error handling for not found resources.

2. models.py: This file defines the SQLAlchemy models for Restaurant, Pizza, and RestaurantPizza. These models represent the database tables and their relationships.

3. seed.py: This script is used to populate the database with sample data. It generates random restaurant names, addresses, pizza names, and ingredients using the Faker library and adds them to the respective database tables.

## Usage

* Clone this repository to your local machine.
* Create a virtual environment and install the required dependencies listed in requirements.txt.
* Run the Flask application by executing python app.py.
* Access the API using the specified endpoints and methods.

## Installation

1. Run:
pipenv install flask-migrate 
2. In app.py.
from flask_migrate import Migrate
migrate = Migrate(app, db)
db.init_app(app)
3. Run to create database:
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
flask db init 
flask db migrate -m "Initial migration"
flask db upgrade
4. Update db with tables:
flask db revision --autogenerate -m'Create tables owners, pets'

## Author
Valerie Kandagor

###  Github
'''bash
https://github.com/Reiney4/La-pizza
'''
