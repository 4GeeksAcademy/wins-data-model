from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50), unique=True)

    comments = relationship("Comment", back_populates="author")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }


class Comment(db.Model):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(50))
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))

    author = relationship("User", back_populates="comments")

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }


class Post(db.Model):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }


class Media(db.Model):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(Enum("image", name="media_types"))
    url = Column(String())
    post_id = Column(Integer, ForeignKey("post.id"))

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }


class Follower(db.Model):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }
