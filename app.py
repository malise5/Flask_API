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


# Decorator
@app.route('/')
def index():
    return '<h1>Hallo World!!</h1>'


@app.route('/image')
def image():
    return '<h1>This is an image</h1>'


# run the following in the terminal/shell
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555

# for creatind db migartion
# flask db init
# flask db revision --autogenerate -m "create production table"
# flask db upgrade


# flask run --debug
