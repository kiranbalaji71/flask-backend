from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Kiran Balaji/Download/flask-backend/DAY02_Flask_Auth_JWT/pydatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Kiran Balaji/Desktop/Project/flask-backend/DAY02_Flask_Auth_JWT/pydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = '58d253a6143302be77a5d223060de63ff912d23048cb950fea8270fc3d9198ae8b04ba762269d89c0d57f54eed054133fb490115951006c245cccf760b96c6f7'  

db = SQLAlchemy(app)
jwt = JWTManager(app)
