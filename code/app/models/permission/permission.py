from flask import current_app as app
from app.extensions import db
from enum import Enum
from sqlalchemy.ext.hybrid import hybrid_property


# factor out (business logic)?
class PermissionEnum(Enum):
    VIEW_BOOKING = 'VIEW_BOOKING'
    MAKE_BOOKING = 'MAKE_BOOKING'
    EDIT_BOOKING = 'EDIT_BOOKING'
    CANCEL_BOOKING = 'CANCEL_BOOKING'

    VIEW_OTHERS_BOOKING = 'VIEW_OTHERS_BOOKING'
    MAKE_OTHERS_BOOKING = 'MAKE_OTHERS_BOOKING'
    EDIT_OTHERS_BOOKING = 'EDIT_OTHERS_BOOKING'
    CANCEL_OTHERS_BOOKING = 'CANCEL_OTHERS_BOOKING'

    VIEW_USER = 'VIEW_USER'
    CREATE_USER = 'CREATE_USER'
    EDIT_USER = 'EDIT_USER'
    DELETE_USER = 'DELETE_USER'

    VIEW_OTHER_USER = 'VIEW_OTHER_USER'
    CREATE_OTHER_USER = 'CREATE_OTHER_USER'
    EDIT_OTHER_USER = 'EDIT_OTHER_USER'
    DELETE_OTHER_USER = 'DELETE_OTHER_USER'

    # TODO: add more as needed


class Permission(db.Model):
    '''
    Database representation of a permission
    '''
    __tablename__ = 'permission'

    _id = db.Column('id', db.Integer, primary_key=True)
    _name = db.Column('name', db.String(120), unique=True, nullable=False)

    def __init__(self, name):
        self._name = name

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __repr__(self):
        return '<Permission %r>' % self._name
