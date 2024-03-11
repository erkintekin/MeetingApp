from flask import Flask

def create_app():
    app=Flask(__name__)
    # Encrypt cookies and session datas
    app.config['SECRET KEY'] = 'abcd'

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # To go the defined page
    

    return app
