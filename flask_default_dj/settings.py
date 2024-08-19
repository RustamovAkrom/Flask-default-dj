from flask import Flask
from .utils import generate_secret_key

def default_config(app: Flask) -> Flask:
    app.config['SECRET_KEY'] = generate_secret_key()
    app.config['DEBUG'] = True
    app.config['TESTING'] = False
    app.config['INSTALLED_APPS'] = []
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_default_dj.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['BCRYPT_LOG_ROUNDS'] = 12
    app.config['BCRYPT_HASH_PREFIX'] = '2b'
    app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = False
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
    app.config['UPLOADS_DEFAULT_DEST'] = 'media'
    app.config['UPLOADS_DEFAULT_URL'] = 'media'
    app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024
    
    return app

def default_test_config(app: Flask):
    app = default_config(app)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tests.db"
    app.config['WTF_CSRF_ENABLED'] = False