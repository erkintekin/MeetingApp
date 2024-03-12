from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager  # Manage the logins

# Naming the database
db = SQLAlchemy()
DB_NAME = "meetingApp.db"



def create_app():
    app=Flask(__name__)

    # Encrypt cookies and session datas
    app.secret_key = 'abcd1234'

    # Adding SQLAlchemy location, using f prime for SQLite connection
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 

    # Database initialization
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # To go the defined page

        # Defining the model tables
    from .models import User, MeetingData

        # To create database with SQLAlchemy
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # If user is not logged in
    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # Flask will find the user by its ID which is primary key

    return app

    