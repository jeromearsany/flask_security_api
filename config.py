import os

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "3308"))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "123456")
    DB_NAME = os.getenv("DB_NAME", "security_db")
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")
