from flask import current_app as app
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property

from app.models.role import Role, RoleEnum
from app.models.user import UserDetails


class User(db.Model):
    '''
    Database representation of a login
    '''
    __tablename__ = 'users'

    _id = db.Column('id', db.Integer, primary_key=True)
    _email = db.Column('email', db.String(120), unique=True, nullable=False)
    _password_hash = db.Column('password_hash', db.String(128), nullable=False)
    _role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.id'), nullable=False)
    _user_details_id = db.Column('user_details_id', db.Integer, db.ForeignKey('user_details.id'))

    _role = db.relationship('Role')
    _details = db.relationship('UserDetails')
    def __init__(self, email, password=None, role=None, details=None):
        self._email = email
        if password is not None:
            self.password = password
        self._role = role
        self._details = details

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @hybrid_property
    def password(self):
        raise NotImplementedError

    @password.setter
    def password(self, value):
        self._password_hash = generate_password_hash(value)

    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)

    @hybrid_property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @hybrid_property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    def __repr__(self):
        return '<User %r>' % self._email
