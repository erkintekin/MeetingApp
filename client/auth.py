from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db  # For sessions
from werkzeug.security import generate_password_hash, check_password_hash  # To hash a password for security (SHA-256)
from flask_login import login_user, login_required, logout_user, current_user # current_user comes from UserMixin

auth = Blueprint('auth',__name__)

# To allow get & post methods
@auth.route('/login', methods=['GET','POST']) 
def login():
        if request.method == 'POST':
                email = request.form.get('email')
                password = request.form.get('password')
                user = User.query.filter_by(email=email).first() # e-mail is unique
                if user:
                        if check_password_hash(user.password, password):
                                flash('Login successful!',category='successs')
                                login_user(user, remember=True)
                                return redirect(url_for('views.home'))
                        else:
                                flash('Login failed! Incorrect password', category='error')        
                else:
                        flash('Login failed! Check your e-mail adress',category='error')

        return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required # It makes logout page inaccessible unless the user is not logged in
def logout():
        logout_user()
        return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def signUp():
        if request.method == 'POST':
                email = request.form.get('email')
                firstName = request.form.get('firstName')
                password1 = request.form.get('password1')
                password2 = request.form.get('password2')
                
                user = User.query.filter_by(email=email).first()

                if user:
                        flash('This e-mail already exists!, try another e-mail to sign-up', category='error')
                elif len(email) < 3:
                        flash('E-mail must be greater than 2 characters.', category='error')
                elif len(firstName) < 2:
                        flash('First name must be greater than 1 characters.', category='error')
                elif password1 != password2:
                        flash('Password must match. Check again?', category='error')
                elif len(password1) < 8:
                        flash('Password must be at least 8 characters.', category='error')
                else:
                       # Successfully signed up
                       new_user = User(email=email,first_name=firstName,password=generate_password_hash(password1, method='sha256'))
                       db.session.add(new_user)
                       db.session.commit()
                       login_user(new_user, remember=True)
                       flash('User created', category='success')
                       return redirect(url_for('views.home'))

        else:
                flash('Please fill out the sign-up form.', category='error')
        return render_template("sign_up.html", user=current_user)