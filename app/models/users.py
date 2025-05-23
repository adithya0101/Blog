from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.model):
    __tablename__='Users'

    uuid=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(10))
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)
    bio=db.column(db.String(100), nullable=True)

