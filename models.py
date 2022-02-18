from alchemy_repositories import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.Text(),nullable=False)
    email = db.Column(db.Text(),nullable=False)
    password = db.Column(db.Text(), nullable=False)