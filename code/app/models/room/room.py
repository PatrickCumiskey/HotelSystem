from flask import current_app as app
from app.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property


class Room(db.Model):
    '''
    Database representation of a room
    '''
    __tablename__ = 'rooms'

    _id = db.Column('id', db.Integer, primary_key=True)
    _type = db.Column('type', db.Integer, db.ForeignKey('room_price.id'), nullable=False)
    _number = db.Column('number', db.Integer, nullable=False)
    _occupancy = db.Column('occupancy', db.Integer, nullable=False)
    _availability = db.Column('availability', db.String(120), nullable=False)
    _clean = db.Column('clean', db.Boolean, nullable=False)

    _room_price = db.relationship('RoomPrice')
    def __init__(self, type, number, occupancy, availability, clean):
        self._type = type
        self._number = number
        self._occupancy = occupancy
        self._availability = availability
        self._clean = clean

    @hybrid_property
    def type(self):
        return self._type

    @hybrid_property
    def id(self):
        return self._id

    @type.setter
    def type(self, value):
        self._type = value

    @hybrid_property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @hybrid_property
    def occupancy(self):
        return self._occupancy

    @occupancy.setter
    def occupancy(self, value):
        self._occupancy = value

    @hybrid_property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        self._availability = value

    @hybrid_property
    def clean(self):
        return self._clean

    @clean.setter
    def clean(self, value):
        self._clean = value

    @hybrid_property
    def room_price(self):
        return self._room_price

    @room_price.setter
    def room_price(self, value):
        self._room_price = value

    def __repr__(self):
        return '<Room %r:%r:%r>' % (self._id, self._type, self._number)