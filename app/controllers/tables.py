from email.policy import default
from enum import unique
from sqlalchemy import null
from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    name = db.Column(db.String(40), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

db.create_all()