from flask import Flask

APP = None

def register_error_handlers(app: Flask):
    global APP
    APP = app

    pass