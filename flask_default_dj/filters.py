from flask import Flask

APP = None

def register_filters(app: Flask):
    global APP
    APP = app
    
    @app.template_filter("reverse")
    def reverse_filter(s):
        return s[::-1]
    