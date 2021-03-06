from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from uuid import uuid4
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash
from datetime import datetime


db = SQLAlchemy()
login = LoginManager()


@login.user_loader
def load_user(userid):
    return User.query.get(userid)

class User(db.Model, UserMixin):
    id = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password =db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))
    characters = db.relationship('MarvelCharacter', backref='owner')

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password) 

class MarvelCharacter(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(400), nullable=False)
    comics_appeared_in = db.Column(db.Integer)
    super_power = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    owner_id = db.Column(db.String(80), db.ForeignKey('user.id'))


    def __init__(self, dict, owner_id):
        self.id = str(uuid4())
        self.name = dict['name']
        self.description = dict['description']
        self.super_power = dict['super_power']
        self.comics_appeared_in = dict.get('comics_appeared_in', 0)
        self.owner_id = owner_id



    def to_dict(self):
            return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'super_power': self.super_power,
                'comics_appeared_in': self.comics_appeared_in
            }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])
   
