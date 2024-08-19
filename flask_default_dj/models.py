from flask_default_dj.extensions import db, bcrypt
from flask_login import UserMixin


class UserModel(db.Model):
    __abstract__ = True
    
    first_name = db.Column(db.String(120), name="first_name", nullable=True)
    last_name = db.Column(db.String(120), name="last_name", nullable=True)
    username = db.Column(db.String(150), name="username", nullable=False, unique=True, index=True)
    email = db.Column(db.String(256), name="email", nullable=True, index=True)
    password = db.Column(db.String(300), name="password", unique=True)
    is_superuser = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")


class BaseUserModel(UserMixin, UserModel):
    __tablename__ = "base_user_models"
    
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self) -> str:
        return f"<User {self.username}>"

