from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Kiran Balaji/Download/flask-backend/DAY01_Flask_Basics/pydatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Kiran Balaji/Desktop/Project/flask-backend/DAY01_Flask_Basics/pydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
