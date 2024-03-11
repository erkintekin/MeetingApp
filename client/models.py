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
    date = db.Column(db.Date)
    start_time = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))
        # A meeting can have many participants
    participants = relationship('User', secondary='user_meeting', backref='meetings')


class User(db.Model, UserMixin):
        # ID column will be the primary key.
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128), unique=True) # Unique
    password = db.Column(db.String(20))
    first_name = db.Column(db.String(128))



class UserMeeting(db.Model):
        # This statement references to the user_meeting table at the database.
    __tablename__ = 'user_meeting'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting_data.id'), primary_key=True)