from flask import Flask
from config import Config
from .auth.routes import auth
from .models import db, login
from flask_migrate import Migrate
##This code below instantiates the flask app with the name 
##From what I understand, this file will be instantiated first
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth)
login.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)

from . import routes