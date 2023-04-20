from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate

from flask_restful import Api, Resource

# error handling
from werkzeug.exceptions import NotFound

from models import db, Production, CastMember

# initialize the App
app = Flask(__name__)
# connects to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # avoid an error
app.json.compact = False

# migration
migrate = Migrate(app, db)
db.init_app(app)  # initialize the application with sqlalchemy

# initialize Api
api = Api(app)

# create a GET all Route for Production


class Productions(Resource):
    def get(self):
        production_list = [production.to_dict()
                           for production in Production.query.all()]

        response = make_response(
            production_list,
            200
        )
        return response

# make a post request
    def post(self):
        request_json = request.get_json()
        new_production = Production(
            title=request_json["title"],
            genre=request_json["genre"],
            budget=request_json["budget"],
            image=request_json["image"],
            director=request_json["director"],
            description=request_json["description"],
            ongoing=request_json["ongoing"],

        )
        db.session.add(new_production)
        db.session.commit()

        response = make_response(
            new_production.to_dict(),
            201
        )

        return response


api.add_resource(Productions, '/productions')

# GET ONE ROUTE OF PRODUCTIONS


class ProductionByID(Resource):
    def get(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abort(404, 'The production is not available')

        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            200
        )
        return response

# patch the production by id
    def patch(self, id):
        production = Production.query.filter_by(id=id).first()

        if not production:
            abort(404, 'the production you want to update was not found')

        request_json = request.get_json()
        for key in request_json:
            setattr(production, key, request_json[key])

        db.session.add(production)
        db.session.commit()

        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            201
        )

        return response


# delete the production by id

    def delete(self, id):
        production = Production().query.filter_by(id=id).first()
        if not production:
            abort(404, "The production you are trying to delete can not be found")

        db.session.delete(production)
        db.session.commit()

        response = make_response(
            "Production Deleted Succesfully",
            204
        )

        return response


api.add_resource(ProductionByID, '/productions/<int:id>')


# GET ALL CastMembers


class CastMembers(Resource):

    # getting all the cast memebers
    def get(self):
        cast_memebers_list = [
            cast_memeber.to_dict() for cast_memeber in CastMember.query.all()
        ]
        response = make_response(
            cast_memebers_list,
            200
        )
        return response

# posting new  cast memebers

    def post(self):
        request_json = request.get_json()
        new_castmember_json = CastMember(
            name=request_json['name'],
            role=request_json['role'],
            production_id=request_json['production_id']
        )
        db.session.add(new_castmember_json)
        db.session.commit()

        response = make_response(
            new_castmember_json.to_dict(),
            201
        )

        return response


api.add_resource(CastMembers, '/cast_members')


# GET ONE ROUTE OF cast member

class CastMemberByID(Resource):

    # getting all the cast memebers by id

    def get(self, id):
        # cast_member = CastMember.query.filter(CastMember.id == id).first()
        cast_member = CastMember.query.filter_by(id=id).first()

        if not cast_member:
            abort(404, 'The Cast Member is not available')
        cast_member_dict = cast_member.to_dict()

        response = make_response(
            cast_member_dict,
            200
        )
        return response

# patching  cast memebers by id

    def patch(self, id):

        cast_member = CastMember.query.filter_by(id=id).first()

        if not cast_member:
            abort(404, 'Cant find the cast member')

        request_json = request.get_json()
        for key in request_json:
            setattr(cast_member, key, request_json[key])

        db.session.add(cast_member)
        db.session.commit()

        cast_member_dict = cast_member.to_dict()
        response = make_response(
            cast_member_dict,
            201
        )

        return response


# delete the production by id


    def delete(self, id):
        cast_member = CastMember.query.filter_by(id=id).first()
        if not cast_member:
            abort(404, "The cast Member you are trying to delete can not be found")

        db.session.delete(cast_member)
        db.session.commit()

        response = make_response(
            "Cast_Member Deleted Succesfully",
            204
        )

        return response


api.add_resource(CastMemberByID, '/cast_members/<int:id>')


# error handling


@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "NotFound: Sorry the resource you are looking for can not be found",
        404
    )
    return response


# run the following in the terminal/shell
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555

# for creatind db migartion
# flask db init
# flask db revision --autogenerate -m "create production table"
# flask db upgrade


# flask run --debug
