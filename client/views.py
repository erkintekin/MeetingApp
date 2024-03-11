from flask import Blueprint, render_template

views = Blueprint('views',__name__)


@views.route('/')
def home():
    # Routing the homepage
    return render_template("home.html") 

@views.route('/login')
def login():
    # Routing the login
    return render_template("login.html") 

@views.route('/sign-up')
def signUp():
    # Routing the sign up page
    return render_template("sign_up.html") 

