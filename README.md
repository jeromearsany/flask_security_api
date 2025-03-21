# Flask Security API

This is a simple API built with Flask and MySQL. It allows users to **sign up, log in**, and manage products. The API uses **JWT tokens** to secure access.

---

## 📌 Features
- **User Authentication** using JWT tokens  
- **Password Hashing** for security  
- **CRUD Operations** for managing products  
- **MySQL Database** for storing users and products  
- **Flask Framework** for backend development  

---

## 🚀 How to Set Up

### **1️⃣ Install Required Software**
Make sure you have:
- [**Python (3.x)**](https://www.python.org/downloads/) installed  
- [**XAMPP**](https://www.apachefriends.org/) installed (for MySQL)  
- [**Git**](https://git-scm.com/downloads) installed  
- [**VS Code**](https://code.visualstudio.com/) installed  

---

### **2️⃣ Download the Project**
1. Open **VS Code Terminal**.  
2. Run this command to download the project:
   ```sh


---

3️⃣ Create a Virtual Environment

1. Run this command:

python -m venv venv


2. Activate the virtual environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate





---

4️⃣ Install Required Python Packages

Run this command to install the required libraries:

pip install -r requirements.txt


---

5️⃣ Configure the .env File

1. Create a new file named .env inside the project folder.


2. Copy and paste this inside the file:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=security_db
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key


3. Replace your_secret_key and your_jwt_secret_key with random secure keys.




---

6️⃣ Set Up the MySQL Database

1. Open XAMPP Control Panel and start Apache & MySQL.


2. Open phpMyAdmin in your browser:

http://localhost/phpmyadmin


3. Create a new database named security_db.


4. Click SQL and copy-paste this code:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    pid INT AUTO_INCREMENT PRIMARY KEY,
    pname VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


5. Click Go to run the query.




---

7️⃣ Run the Flask App

Run this command in the terminal:

python app.py

The API will now run at:

http://127.0.0.1:5000


---

📌 API Endpoints


---

🔒 How to Use the API

1️⃣ Register a User

Send a POST request to /signup with this JSON data:

{
    "name": "John Doe",
    "username": "johndoe",
    "password": "securepassword"
}

2️⃣ Log In to Get a JWT Token

Send a POST request to /login with:

{
    "username": "johndoe",
    "password": "securepassword"
}

Response:

{
    "token": "your_generated_jwt_token"
}

Copy the token because you'll need it to access protected routes.

3️⃣ Use JWT Token in Requests

For all product operations, include this Authorization header in your requests:

Authorization: Bearer your_generated_jwt_token


---

📌 Running the App in Debug Mode

Use:

python app.py

or:

FLASK_ENV=development flask run


---

🛠 Troubleshooting

Problem: MySQL Connection Issues

Check if XAMPP MySQL is running.

Make sure your database name and credentials in .env are correct.


Problem: Flask Command Not Found

Activate the virtual environment and try again.

Run:

pip install flask
