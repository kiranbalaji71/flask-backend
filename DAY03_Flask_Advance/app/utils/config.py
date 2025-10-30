import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///pydatabase.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "app/static/uploads")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
