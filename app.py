from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from flask_restful import Api, Resource

from models import db, Production, CastMember

# initialize the App
app = Flask(__name__)
# connects to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # avoid an error

# migration
migrate = Migrate(app, db)
db.init_app(app)  # initialize the application with sqlalchemy

# initialize Api
api = Api(app)

# create a GET all Route


class Productions(Resource):
    def get(self):
        # production_list = [{
        #     "title": production.title,
        #     "genre": production.genre,
        #     "budget": production.budget,
        #     "image": production.image,
        #     "director": production.director,
        #     "description": production.description,
        #     "ongoing": production.ongoing,
        # }for production in Production.query.all()]

        production_list = [production.to_dict()
                           for production in Production.query.all()]

        response = make_response(
            production_list,
            200
        )
        return response


api.add_resource(Productions, '/productions')

# GET ALL CastMembers


class CastMembers(Resource):
    def get(self):
        cast_memebers_list = [
            cast_memeber.to_dict() for cast_memeber in CastMember.query.all()
        ]
        response = make_response(
            cast_memebers_list,
            200
        )
        return response


api.add_resource(CastMembers, '/cast_members')


# run the following in the terminal/shell
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555

# for creatind db migartion
# flask db init
# flask db revision --autogenerate -m "create production table"
# flask db upgrade


# flask run --debug
