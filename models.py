from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# validation
from sqlalchemy.orm import validates

db = SQLAlchemy()

# CREATING THE TABLE MODEL


class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

# COLUMNS OF THE TABLE
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # extra column to link productions to cast memebers
    cast_members = db.relationship('CastMember', backref='production')

    # serializer rule that will help add our 'cate_member' to the response
    # serialize_only = ('title',)
    serialize_rules = ('-cast_members.production',
                       '-created_at', '-updated_at')


# use "validates" decorator to create a validation for images

    @validates('image')
    def validates_image(self, key, image_path):
        if '.jpg' not in image_path:
            raise ValueError("Image must be a .jpg")
        return image_path


# DISPLAYS ALL THE DATA FOR PRODUCTION TABLE


    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director}, Description:{self.description}, Ongoing:{self.ongoing}'


# castmemebers table
class CastMember(db.Model, SerializerMixin):
    __tablename__ = 'castmembers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # foreignkey
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))

    # serializer rule that will help add our 'cate)member' to the response
    serialize_rules = ('-production.cast_member', '-created_at', '-updated_at')

    # DISPLAYS ALL THE DATA FOR PRODUCTION TABLE
    def __repr__(self):
        return f'<CastMember Name:{self.name}, Role:{self.role}'


# GO TO APP.PY
