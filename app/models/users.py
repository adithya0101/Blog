from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.model)