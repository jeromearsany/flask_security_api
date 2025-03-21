from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db, cursor

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products", methods=["POST"])
@jwt_required()
def add_product():
    data = request.json
    try:
        cursor.execute("INSERT INTO products (pname, description, price, stock) VALUES (%s, %s, %s, %s)",
                       (data["pname"], data["description"], data["price"], data["stock"]))
        db.commit()
        return jsonify({"message": "Product added"}), 201
    except Exception as e:
        return jsonify({"error": "Invalid product data or database error"}), 400

@product_routes.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return jsonify(products) if products else jsonify({"message": "No products found"})

@product_routes.route("/products/<int:pid>", methods=["GET"])
@jwt_required()
def get_product(pid):
    try:
        cursor.execute("SELECT * FROM products WHERE pid = %s", (pid,))
        product = cursor.fetchone()
        if product:
            return jsonify(product)
        return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_routes.route("/products/<int:pid>", methods=["PUT"])
@jwt_required()
def update_product(pid):
    cursor.execute("SELECT * FROM products WHERE pid = %s", (pid,))
    if not cursor.fetchone():
        return jsonify({"error": "Product not found"}), 404
    
    data = request.json
    cursor.execute("UPDATE products SET pname=%s, description=%s, price=%s, stock=%s WHERE pid=%s",
                   (data["pname"], data["description"], data["price"], data["stock"], pid))
    db.commit()
    return jsonify({"message": "Product updated"})

@product_routes.route("/products/<int:pid>", methods=["DELETE"])
@jwt_required()
def delete_product(pid):
    cursor.execute("SELECT * FROM products WHERE pid = %s", (pid,))
    if not cursor.fetchone():
        return jsonify({"error": "Product not found"}), 404
    
    cursor.execute("DELETE FROM products WHERE pid=%s", (pid,))
    db.commit()
    return jsonify({"message": "Product deleted"})
