import uuid

import flask_bcrypt
from flask_login import UserMixin
from init_dba import db
from datetime import datetime

class User(db.Model, UserMixin):
    _password = db.Column(db.LargeBinary)
    id = db.Column(db.String(300), primary_key=True, default=uuid.uuid4())
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password):
        return flask_bcrypt.check_password_hash(self._password, password)

class Operation(db.Model):
    id = db.Column(db.String(300), primary_key=True, default=uuid.uuid4())
    name = db.Column(db.String(200), nullable=False, unique=False)
    data = db.Column(db.Datetime, nullable=False)
    operators = db.Column(db.ARRAY(db.String(100)), nullable=False)
    body = db.Culumn(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
