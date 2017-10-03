from flask import current_app as app
from app.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property

class RoomStatus(db.Model):
    '''
    Database representation of dates and rooms left
    '''
    __tablename__ = 'room_status'
    _id = db.Column('id', db.Integer, primary_key=True)
    _date = db.Column('date', db.Date, nullable=False)
    _type = db.Column('type', db.Integer, db.ForeignKey('room_price.id'), nullable=False)
    _qty = db.Column('qty', db.Integer, nullable=False)

    _room_price = db.relationship('RoomPrice')


    def __init__(self, date, type, qty):
        self._date = date
        self._type = type
        self._qty = qty

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def date(self):
        return self._date

    @hybrid_property
    def type(self):
        return self._type

    @hybrid_property
    def qty(self):
        return self._qty

    @date.setter
    def date(self, value):
        self._date = value

    @type.setter
    def type(self, value):
        self._type = value

    @qty.setter
    def qty(self, value):
        self._qty = value

    @hybrid_property
    def room_price(self):
        return self._room_price

    def __repr__(self):
        return '<Date:%r \nType: %r Remaining: %r >' % (self._date, self._type, self._qty)
