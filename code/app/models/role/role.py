from flask import current_app as app
from app.extensions import db
from enum import Enum
from sqlalchemy.ext.hybrid import hybrid_property

from app.models.permission import Permission, PermissionEnum


class RoleEnum(Enum):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    STAFF = 'STAFF'
    GUEST = 'GUEST'
    ANONYMOUS = 'ANONYMOUS'


'''
Many to many relationship between roles and permissions
'''
role_permission = db.Table(
    'role_permission',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), nullable=False),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), nullable=False),
    db.PrimaryKeyConstraint('role_id', 'permission_id')
)


class Role(db.Model):
    '''
    Database representation of a role
    '''
    __tablename__ = 'role'

    _id = db.Column('id', db.Integer, primary_key=True)
    _name = db.Column('name', db.String(120), unique=True, nullable=False)

    _permissions = db.relationship('Permission', secondary=role_permission, backref='roles')

    def __init__(self, name, permissions=None):
        self.name = name
        if permissions is not None:
            self._permissions = permissions

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @hybrid_property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        self._permissions = value

    def __repr__(self):
        return '<Role %r>' % self.name
