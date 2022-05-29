import os

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__name__))
SQLALCHEMY_DATABASE_URI = os.environ.get('SQUALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
class Config:
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    