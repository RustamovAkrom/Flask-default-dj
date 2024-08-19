from flask import Flask
from flask_default_dj.extensions import db, login_manager
from flask_default_dj.extensions import (
    init_db, 
    init_migrate, 
    init_login_manager, 
    init_bcrypt, 
    init_babel, 
    init_admin,
    init_mail,
    init_bootstrap
)
from .cli import register_cli_commands
from .errors import register_error_handlers
from .filters import register_filters
from .blueprints import register_blueprints
from .apps import register_installed_apps
from .models import BaseUserModel
from .settings import default_config


APP = None

def create_app(app: Flask = None) -> Flask | None:
    global APP
    APP = app
    
    init_db(app)    
    init_migrate(app, db)
    init_login_manager(app)
    init_bcrypt(app)
    init_babel(app)
    init_admin(app)
    init_mail(app)
    init_bootstrap(app)

    register_cli_commands(app)
    register_error_handlers(app)
    register_filters(app)
    register_blueprints(app)
    register_installed_apps(app)

    @login_manager.user_loader
    def load_user(user_id):
        return BaseUserModel.query.get(int(user_id))

    return app

base_app = Flask(__name__)
base_app.config.from_object(default_config(base_app))
application = create_app(base_app)

__all__ = ("create_app", )