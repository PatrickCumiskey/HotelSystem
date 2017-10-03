from app.extensions import db
from config import TestConfig
from test import BaseDatabaseTest
from datetime import datetime
from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager
from app.api.user_manager import UserManager
from app.models.user import User
from app.models.user import UserDetails
from app.models.room import RoomPrice
from app.models.room import Room
from app.models.booking import Booking
from app.api.booking_manager import cancelBooking, makeBooking
import datetime



class TestBookingManger(BaseDatabaseTest):
    @classmethod
    def setup_class(cls):
        super(TestBookingManger, cls).setup_class()


    @classmethod
    def teardown_class(cls):
        with cls.app.app_context():
            db.drop_all()

    def pricechange_test(self):
        with self.app.app_context():
            result = RoomManager.pricechange(1,1235,4565)
            assert result != False

    def bookingcancel_test(self):
        with self.app.app_context():
            cancelBooking.bookingcancel(1, 123123123, 101, '20170102')
