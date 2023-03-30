import uuid

import flask_bcrypt
from flask_login import UserMixin
from models.init_dba import db
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey


_operation_surgeon_table = db.Table(
    'operation_surgeon_table',
    db.metadata,
    db.Column('operation_id', String(300), ForeignKey('operations.id',
                                                            ondelete='CASCADE'),
              nullable=False),
    db.Column('surgeon_id', String(300), ForeignKey('surgeons.id',
                                                            ondelete='CASCADE'),
              nullable=False)
)
_operation_nurse_table = db.Table(
    'operation_nurse_table',
    db.metadata,
    db.Column('operation_id', String(300), ForeignKey('operations.id',
                                                           ondelete='CASCADE')),
    db.Column('nuse_id', String(300), ForeignKey('nurses.id',
                                                           ondelete='CASCADE')),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

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
    __tablename__ = 'operations'

    id = db.Column(db.String(300), primary_key=True,
                   default=lambda: uuid.uuid4(), unique=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    data = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    surgeons = relationship('Surgeon',
                           secondary=_operation_surgeon_table,
                           back_populates='operations',
                           uselist=True)
    nurse = relationship('Nurse',
                        secondary=_operation_nurse_table,
                        back_populates='operations',
                        uselist=True)


class Nurse(db.Model):
    __tablename__ = 'nurses'

    id = db.Column(db.String(300), primary_key=True,
                   default=lambda: uuid.uuid4(), unique=True)
    first_name = db.Column(db.String(200), nullable=False, unique=False)
    second_name = db.Column(db.String(200), nullable=False, unique=False)
    last_name = db.Column(db.String(200), nullable=False, unique=False)

    operations = relationship('Operation',
                              secondary=_operation_nurse_table,
                              back_populates='nurse',
                              uselist=True)

class Surgeon(db.Model):
    __tablename__ = 'surgeons'

    id = db.Column(db.String(300), primary_key=True,
                   default=lambda: uuid.uuid4(), unique=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    first_name = db.Column(db.String(200), nullable=False, unique=False)
    second_name = db.Column(db.String(200), nullable=False, unique=False)
    last_name = db.Column(db.String(200), nullable=False, unique=False)

    operations = relationship('Operation',
                              secondary=_operation_surgeon_table,
                              back_populates='surgeons',
                              uselist=True)
