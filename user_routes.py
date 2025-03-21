from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from database import db, cursor

user_routes = Blueprint("user_routes", __name__)
bcrypt = Bcrypt()  # Initialize bcrypt inside this file

@user_routes.route("/signup", methods=["POST"])
def signup():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    
    try:
        cursor.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)",
                       (data["name"], data["username"], hashed_password))
        db.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Username already exists or invalid data"}), 400

@user_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    cursor.execute("SELECT * FROM users WHERE username = %s", (data["username"],))
    user = cursor.fetchone()

    if user and bcrypt.check_password_hash(user["password"], data["password"]):
        token = create_access_token(identity=str(user["id"]), expires_delta=timedelta(minutes=10))
        return jsonify({
            "token": token,
            "user_id": user["id"],
            "username": user["username"]
        })
    return jsonify({"error": "Invalid username or password"}), 401
