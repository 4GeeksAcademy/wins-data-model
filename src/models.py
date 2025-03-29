from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(50))
    firstname = mapped_column(String(50))
    lastname = mapped_column(String(50))
    email = mapped_column(String(50), unique=True)

def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }

class Post(db.Model):
    __tablename__ = "post"
    def serialize(self):
        return {
        }
    
class Media(db.Model):
    __tablename__ = "media"
    def serialize(self):
        return {
        }
    
class Follower(db.Model):
    __tablename__ = "follower"
    def serialize(self):
        return {
        }
