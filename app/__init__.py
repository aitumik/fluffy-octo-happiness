from flask import flask
from flask_boostrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(ap[])

    return app