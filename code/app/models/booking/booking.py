from flask import current_app as app
from app.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property


class Booking(db.Model):
    '''
    Database representation of bookings
    '''
    __tablename__ = 'bookings'

    _id = db.Column('id', db.Integer, primary_key=True)
    _user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False)
    _room_id = db.Column('room_id', db.Integer, db.ForeignKey('rooms.id'),  nullable=False)
    _start_date = db.Column('start_date', db.Date, nullable=False)
    _end_date = db.Column('end_date', db.Date, nullable=False)
    _credit_card = db.Column('credit_card', db.Integer, nullable=False)
    _booking_price = db.Column('booking_price', db.Float, nullable=False)

    _user = db.relationship('User')
    _room = db.relationship('Room')

    def __init__(self, user_id, room_id, start_date, end_date, credit_card, booking_price):
        self._user_id = user_id
        self._room_id = room_id
        self._start_date = start_date
        self._end_date = end_date
        self._credit_card = credit_card
        self._booking_price = booking_price
    @hybrid_property
    def user(self):
        return self._user
    @hybrid_property
    def room(self):
        return self._room
    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @hybrid_property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value

    @hybrid_property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @hybrid_property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @hybrid_property
    def credit_card(self):
        return self._credit_card

    @credit_card.setter
    def credit_card(self, value):
        self._credit_card = value

    @hybrid_property
    def booking_price(self):
        return self._booking_price

    @booking_price.setter
    def booking_price(self, value):
        self._booking_price = value

    @hybrid_property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        self._room = value

    @hybrid_property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value


    def __repr__(self):
        return '<Booking ref %r>' % self._id
