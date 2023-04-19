from flask import Flask, jsonify, make|_response, request
from flask_migrate import Migrate

from models import db, Production

#initialize the App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' #connects to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #avoid an error