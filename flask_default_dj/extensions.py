from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_babel import Babel
from flask_admin import Admin
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask import Flask


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
babel = Babel()
admin = Admin()
mail = Mail()
bootstrap = Bootstrap()
admin.template_mode = "bootstrap3"

def init_db(app: Flask):
    db.init_app(app)

def init_migrate(app: Flask, db: SQLAlchemy):
    migrate.init_app(app, db)

def init_login_manager(app: Flask):
    login_manager.init_app(app)

def init_bcrypt(app: Flask):
    bcrypt.init_app(app)

def init_babel(app: Flask):
    babel.init_app(app)

def init_admin(app: Flask):
    admin.init_app(app)

def init_mail(app: Flask):
    mail.init_app(app)

def init_bootstrap(app: Flask):
    bootstrap.init_app(app)