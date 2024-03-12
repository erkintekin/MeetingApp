# Importation the SQLAlchemy
from . import db 

# flask_login for user login and that inherits from UserMixin
from flask_login import UserMixin  

# For one-to-many table relationship
from sqlalchemy.orm import relationship

class MeetingData(db.Model):
        # ID column will be the primary key.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    date = db.Column(db.String(50))
    start_time = db.Column(db.String(50))
    end_time = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



class User(db.Model, UserMixin):
        # ID column will be the primary key.
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128), unique=True) # Unique
    password = db.Column(db.String(20))
    first_name = db.Column(db.String(128))
    meetings = db.relationship('MeetingData', backref='user', lazy=True)
