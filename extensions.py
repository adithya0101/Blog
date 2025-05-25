from flask_sqlalchemy import SQLAlchemy
from app.config import Config

from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()