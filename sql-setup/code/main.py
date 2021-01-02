from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from bcrypt import hashpw, gensalt

MYSQL_HOST = environ["MYSQL_HOST"] if "MYSQL_HOST" in environ else "localhost"
MYSQL_PORT = environ["MYSQL_PORT"] if "MYSQL_PORT" in environ else "3306"
MYSQL_DB = environ["MYSQL_DB"] if "MYSQL_DB" in environ else "test"
MYSQL_USER = environ["MYSQL_USER"] if "MYSQL_USER" in environ else "root"
MYSQL_PASS = environ["MYSQL_PASS"] if "MYSQL_PASS" in environ else "root"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://" + MYSQL_USER + ":" + MYSQL_PASS + "@" + MYSQL_HOST + ":" + MYSQL_PORT + "/" + MYSQL_DB
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

db.create_all()

admin_pw = "test"
admin = User(name="admin",email="test@dummy.com",password=hashpw(admin_pw.encode(), gensalt()))

db.session.add(admin)
db.session.commit()
