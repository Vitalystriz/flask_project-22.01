from sqlalchemy import update
from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from repositories import get_post
db=SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    comments = db.relationship('Comment')


class Comment(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer(), primary_key=True, unique=True, autoincrement=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    text = db.Column(db.Text(), nullable=False)
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.post_id'))


db.create_all(app=app)
db.session.commit()
def get_all_comments(post_id):
    post = get_post(post_id)
    return post.Comment
def add_comment(post_id,text):
    new_comment = Comment(post_id=post_id, text=text)
    db.session.add(new_comment)
    db.session.commit()
def get_all_posts():
    return Post.query.all()
def get_post(post_id):
    return Post.query.get(post_id)
def get_users(name):
    pass
def insert_into_posts(title,content):
    new_post=Post(title=title,content=content)
    db.session.add(new_post)
    db.session.commit()
# def add_user(name, email, password):
#     new_user=User(name=name,email=email,password=password)
#     db.session.add(new_user)
#     db.session.commit()