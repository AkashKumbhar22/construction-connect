from .extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))  # worker / client

class WorkerProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    service = db.Column(db.String(100))
    city = db.Column(db.String(100))
    areas = db.Column(db.String(200))
    experience = db.Column(db.Integer)
    phone = db.Column(db.String(15))
