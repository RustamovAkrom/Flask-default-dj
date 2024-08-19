from flask import Flask

APP = None

def register_blueprints(app: Flask):
    global APP
    APP = app