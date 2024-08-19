from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()


# Base dir path
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret keys
SECRET_KEY = os.getenv("SECRET_KEY", "jekr058aafpkq4newl6ztzaxfl7ntr")

# Debuging
DEBUG = os.getenv("DEBUG", True)

# Testing 
TESTING = False

# Installed apps
INSTALLED_APPS = [
    "apps.shared"
]

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///sqlite3.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Bcrypt
BCRYPT_LOG_ROUNDS = 12
BCRYPT_HASH_PREFIX = '2b'
BCRYPT_HANDLE_LONG_PASSWORDS = False

# Babel
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_TIMEZONE = "UTC"

# Upload media files
UPLOADS_DEFAULT_DEST = "uploads"
UPLOADS_DEFAULT_URL = "uploads"
MAX_CONTENT_LENGTH = 64 * 1024 * 1024
    