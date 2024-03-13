# Importation the SQLAlchemy
from . import db 

# flask_login for user login and that inherits from UserMixin
from flask_login import UserMixin  

# For one-to-many table relationship
from sqlalchemy.orm import relationship

# For change the style of datetime
from datetime import datetime

class MeetingData(db.Model):
        # ID column will be the primary key.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        # To parse date and time. SQLAlchemy gives an error if i don't use strptime in self method.
    def __init__(self, name, date, start_time, end_time, user_id):
        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.start_time = datetime.strptime(start_time, '%H:%M').time()
        self.end_time = datetime.strptime(end_time, '%H:%M').time()
        self.user_id = user_id


class User(db.Model, UserMixin):
        # ID column will be the primary key.
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128), unique=True) # Unique
    password = db.Column(db.String(20))
    first_name = db.Column(db.String(128))
    meetings = db.relationship('MeetingData', backref='user', lazy=True)
