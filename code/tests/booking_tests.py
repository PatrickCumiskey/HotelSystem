from app.app_factory import AppFactory
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

from app.api.utils import Observable
from app.api.utils import Observer
from app.api.utils import ObserverTest

class AnObserver(Observer):
    def __init__(self):
        self.args = []
        self.kwargs = {}

    def update(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return

class TestBookingView(BaseDatabaseTest):
    @classmethod
    def setup_class(cls):
        super(TestBookingView, cls).setup_class()

        with cls.app.app_context():
            cls.observable = Observable()
            cls.observer1 = AnObserver()

    @classmethod
    def teardown_class(cls):
        super(TestBookingView, cls).teardown_class()

    def test_room_manager(self):
        with self.app.app_context():
            result = RoomManager.set_availability_for_booking(datetime.strptime("2017-01-01", '%Y-%m-%d').date(), 1)
            assert result == False
            result = RoomManager.get_rooms_occupied_on_date("2017-01-01", 1)
            assert result != False

    def test_get_booking_for_user(self):
        with self.app.app_context():
            result = BookingView.get_booking_for_user(1)
            assert result[0]['first_name'] == "mr"
            assert result[0]['last_name'] == "test"

    def test_get_booking_for_credit_card(self):
        with self.app.app_context():
            result = BookingView.get_booking_by_credit_card(123123123)
            assert result[0]['first_name'] == "mr"
            assert result[0]['last_name'] == "test"

    def test_get_sales_between_dates(self):
        with self.app.app_context():
            result = BookingView.get_sales_between_dates("2017-01-01", "2017-01-02")
            assert result[1]['total'] == 2000.0

    def test_room_booked(self):
        with self.app.app_context():
            result = RoomManager.get_rooms_occupied_on_date("2017-01-01", 1)
            assert result['Occupied'] != 0
            result = RoomManager.get_rooms_occupied_on_date("2007-01-01", 1)
            assert result['Occupied'] == 0

    def test_price_from_room_type(self):
        with self.app.app_context():
            result = RoomManager.get_room_price_from_type('single')
            assert result['weekday_price'] == 100
            assert result['weekday_price'] != 0
            assert result['weekend_price'] == 150
            assert result['weekend_price'] != 0

    def test_price_from_room_number(self):
        with self.app.app_context():
            result = RoomManager.get_room_price_from_number(101)
            assert result['weekday_price'] == 100
            assert result['weekday_price'] != 0
            assert result['weekend_price'] == 150
            assert result['weekend_price'] != 0

    def test_get_room_from_number(self):
        with self.app.app_context():
            result = RoomManager.get_room(101)
            assert result != False

    def test_get_room_availability(self):
        with self.app.app_context():
            result = RoomManager.get_room_availablity(101)
            assert result['Room availability'] == 'Available'
            RoomManager.set_room_availablity(101, 'on fire')
            result = RoomManager.get_room_availablity(101)
            assert result['Room availability'] == 'on fire'

    def test_get_room_clean(self):
        with self.app.app_context():
            result = RoomManager.get_room_clean(101)
            assert result['Room clean status'] == True
            RoomManager.set_room_clean(101,  False)
            result = RoomManager.get_room_clean(101)
            assert result['Room clean status'] == False

    def test_observer(self):
        with self.app.app_context():
            self.observable.register(self.observer1)
            self.observable.update_observers('rooms sold out', room=101)
            assert self.observer1.args[0] == 'rooms sold out'
            assert self.observer1.kwargs['room'], 101
            self.observable.unregister_all()

    def test_room_observer(self):
        with self.app.app_context():
            RoomManager.set_availability_for_booking(datetime.strptime("2017-01-01", '%Y-%m-%d').date(), 1)
            RoomManager.set_availability_for_booking(datetime.strptime("2017-01-01", '%Y-%m-%d').date(), 1)
            '''
            use nosetests -vs ./tests to view observer messages
            '''
