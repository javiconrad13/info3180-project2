from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pro2:pro2@localhost/pro2'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vtlfqithrdvtwg:724872cc5ba363a3b46e702d6e24bcc70b4be8bbb02018c62aba528f4a8b4e10@ec2-54-163-254-48.compute-1.amazonaws.com:5432/dciml4nor2868r'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
heroku = Heroku(app)
db = SQLAlchemy(app)


#db.create_all()
from app import views, models

if __name__ == '__main__':
    app.debug = True
    app.run()
