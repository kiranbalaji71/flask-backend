from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os
from app import db
from app.models import User

user_bp = Blueprint("user_bp", __name__)

# Pagination & filtering
@user_bp.route("/", methods=["GET"])
@jwt_required()
def get_users():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("limit", 5))
    search = request.args.get("search", "")

    query = User.query
    if search:
        query = query.filter(User.username.like(f"%{search}%"))

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    users = [u.to_json() for u in pagination.items]

    return jsonify({
        "users": users,
        "total": pagination.total,
        "page": page,
        "pages": pagination.pages
    }), 200


# File upload (profile picture)
@user_bp.route("/upload", methods=["POST"])
@jwt_required()
def upload_file():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"message": "No selected file"}), 400

    filename = secure_filename(file.filename)
    upload_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
    file.save(upload_path)

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    user.profile_pic = f"/static/uploads/{filename}"
    db.session.commit()

    return jsonify({"message": "File uploaded", "profile_pic": user.profile_pic}), 200
