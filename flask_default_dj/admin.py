from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for

from flask_default_dj.extensions import admin


class BaseAdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(admin.url)