from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from app import db
from app.models import User

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username, email, password = data.get("username"), data.get("email"), data.get("password")

    if not username or not email or not password:
        return jsonify({"message": "Missing fields"}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"message": "User already exists"}), 400

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    current_app.logger.info(f"User created: {username}")
    return jsonify({"message": "User created successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username, password = data.get("username"), data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"access_token": token, "user": user.to_json()}), 200
