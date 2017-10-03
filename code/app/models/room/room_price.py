from flask import current_app as app
from app.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property


class RoomPrice(db.Model):
    '''
    Database representation of room prices
    '''
    __tablename__ = 'room_price'

    _id = db.Column('id', db.Integer, primary_key=True)
    _type = db.Column('type', db.String(120), nullable=False)
    _price_weekday = db.Column('price_weekday', db.Float, nullable=False)
    _price_weekend = db.Column('price_weekend', db.Float, nullable=False)

    def __init__(self, type, price_weekday, price_weekend):
        self._type = type
        self._price_weekday = price_weekday
        self._price_weekend = price_weekend

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @hybrid_property
    def price_weekday(self):
        return self._price_weekday

    @price_weekday.setter
    def price_weekday(self, value):
        self._price_weekday = value

    @hybrid_property
    def price_weekend(self):
        return self._price_weekend

    @price_weekend.setter
    def price_weekend(self, value):
        self._price_weekend = value

    def __repr__(self):
        return '<Room %r>' % self._type
