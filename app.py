from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from database import db
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Config)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)

CORS(app)
jwt = JWTManager(app)

# Import routes (Move these imports after initializing `app`)
from routes.user_routes import user_routes
from routes.product_routes import product_routes

app.register_blueprint(user_routes)
app.register_blueprint(product_routes)

if __name__ == "__main__":
    app.run(debug=True)
