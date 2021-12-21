from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["SECRET_KEY"] = "hello"
db = SQLAlchemy(app)


from FlaskProjectPackage import routes
