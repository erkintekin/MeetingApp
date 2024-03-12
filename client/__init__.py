from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Naming the database
db = SQLAlchemy()
DB_NAME = "meetingApp.db"



def create_app():
    app=Flask(__name__)

    # Encrypt cookies and session datas
    app.secret_key = 'abcd1234'

    # Adding SQLAlchemy location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Database initialization
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # To go the defined page

        # Defining the model tables
    from .models import User, MeetingData, UserMeeting

        # To create database with SQLAlchemy
    with app.app_context():
        db.create_all()

    return app

    