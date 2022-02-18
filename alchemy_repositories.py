from sqlalchemy import update
from app import app
from flask_sqlalchemy import SQLAlchemy
from models import Post,User
db=SQLAlchemy(app)
db.session.create_all()
class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.Text(),nullable=False)
    email = db.Column(db.Text(),nullable=False)
    password = db.Column(db.Text(), nullable=False)

def get_all_posts():
    return Post.query.all()

def get_post(post_id):
    return Post.query.get(post_id)
def get_users(user):
    pass
def insert_into_posts(title,content):
    new_post=Post(title=title,content=content)
    db.session.add(new_post)
    db.session.commit()
def add_user(name, email, password):
    new_user=User(name=name,email=email,password=password)
    db.session.add(new_user)
    db.session.commit()