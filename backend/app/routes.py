# backend/app/routes.py
from app import app
from flask import jsonify

@app.route('/')
def home():
    return "Welcome to the Spreadsheet App!"


@app.route("/api/hello", methods=["GET"])
def hello_api():
    return jsonify({"message": "Hello from Flask!"})