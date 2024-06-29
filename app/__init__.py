from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

from app.controllers import default
