from flask_default_dj import create_app
from flask import Flask

# Default flask configurations
app = Flask(__name__)
app.config.from_pyfile("settings.py")

# Creating application
app = create_app(app)

# import apps url
from .urls import *