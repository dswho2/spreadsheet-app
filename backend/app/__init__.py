# backend/app/__init__.py
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Import routes after the app is initialized to avoid circular import
from app import routes