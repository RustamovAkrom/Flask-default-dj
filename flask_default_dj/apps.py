from flask import Flask
from .utils import import_string, check_installed_apps

APP = None

def register_installed_apps(app: Flask):
    global APP
    APP = app
    
    installed_apps = check_installed_apps(app)
    
    for app_name in installed_apps:
        import_app = import_string(app_name)
        
        app.register_blueprint(import_app.BLUEPRINT)