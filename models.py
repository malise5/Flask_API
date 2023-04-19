from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# CREATING THE TABLE MODEL


class Production(db.Model):
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

# DISPLAYS ALL THE DATA FOR PRODUCTION TABLE
    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director}, Description:{self.description}, Ongoing:{self.ongoing}'

# GO TO APP.PY
