from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST']) # To allow get&post methods
def login():
        return render_template("login.html")

@auth.route('/logout')
def logout():
        return render_template("logout.html")

@auth.route('/sign-up',methods=['GET','POST'])
def signUp():
        if request.method == 'POST':
                email = request.form.get('email')
                firstName = request.form.get('firstName')
                password1 = request.form.get('password1')
                password2 = request.form.get('password2')

                if len(email) < 3:
                        flash('E-mail must be greater than 2 characters.', category='error')
                elif len(firstName) < 2:
                        flash('First name must be greater than 1 characters.', category='error')
                elif password1 != password2:
                        flash('Password must match. Check again?', category='error')
                elif len(password1) < 8:
                        flash('Password must be at least 8 characters.', category='error')
                else:
                       # Successfully signed up
                       flash('User created', category='success') 
        else:
                flash('Please fill out the sign-up form.', category='error')
        return render_template("sign_up.html")