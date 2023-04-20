from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db, Production

# initialize the App
app = Flask(__name__)
# connects to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # avoid an error

# migration
migrate = Migrate(app, db)
db.init_app(app)  # initialize the application with sqlalchemy


# Decorator routings
# runs before first request (check if user is logged in)
@app.before_request
def runs_before():
    current_user = {"user_id": 1, "username": "kudez"}
    print(current_user)


@app.route('/')
def index():
    return '<h1>Hallo World!!</h1>'


@app.route('/image')
def image():
    return '<h1>This is an image</h1>'

# dynamic routing
# find by title name


@app.route('/productions/<string:title>')
def production(title):
    production = Production.query.filter(Production.title == title).first()
    production_response = {
        "title": production.title,
        "genre": production.genre,
        "budget": production.budget,
        "image": production.image,
        "director": production.director,
        "description": production.description,
        "ongoing": production.ongoing,
    }
    response = make_response(
        jsonify(production_response),
        200
    )
    return response

# @app.route('/context')
# def context():


# run the following in the terminal/shell
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555

# for creatind db migartion
# flask db init
# flask db revision --autogenerate -m "create production table"
# flask db upgrade


# flask run --debug
