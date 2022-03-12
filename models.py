from alchemy_repositories import db
from datetime import datetime
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

login_manager = LoginManager(app)
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)

class User(db.Model,UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.Text(),nullable=False)
    email = db.Column(db.Text(),nullable=False)
    login = db.Column(db.String(100),nullable=False,unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(),default=datetime.utcnow())