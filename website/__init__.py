import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_NAME = 'etfalytics_db'
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'etfalytics.Uw0ntg3tthIskeyb3c4useItIss3cret.rn7839277462004612543834646'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://etfalytics_db_user:PTHlWrWd7Ycywgg28t9GAYU7E5rxV3ol@dpg-cisitk18g3n42onjre90-a.frankfurt-postgres.render.com/etfalytics_db'
    # postgres://etfalytics_db_user:PTHlWrWd7Ycywgg28t9GAYU7E5rxV3ol@dpg-cisitk18g3n42onjre90-a.frankfurt-postgres.render.com/etfalytics_db
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')