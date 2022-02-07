import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email= Column (String(50),nullable=False, unique=True)
    password= Column(String(20),nullable=False)
    image= Column(String(120))
    bio= Column(String(250))
    followers= Column(Integer, ForeignKey('user.id'))
    followed_users= Column (Integer, ForeignKey('user.id'))
    

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    image_id= Column(String(120), nullable=False)
    text= Column(String(500))
    hashtag=Column(String(20))
    user_id= Column(Integer,ForeignKey('user.id'))
    user=relationship(User)


class Likes(Base):
    __tablename__='likes'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))
    user= relationship(User)
    post= relationship(Post)


class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    text= Column(String(250))
    user_id= Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))
    user= relationship(User)
    post= relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e