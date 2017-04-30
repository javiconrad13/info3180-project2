from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pro2:pro2@localhost/pro2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brsulyexulntlb:f1aa3832a9bae20b12af524f47263b79f92a5316b0b90983f713a4f88f188e1d@ec2-54-235-72-121.compute-1.amazonaws.com:5432/dd8dtciludh0se'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
heroku = Heroku(app)
db = SQLAlchemy(app)


#db.create_all()
from app import views, models

if __name__ == '__main__':
    app.debug = True
    app.run()
