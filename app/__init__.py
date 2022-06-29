from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = sqlalchemy(app)

from app.controllers import default
