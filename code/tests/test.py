# This is a sample test. Create tests in separate files
# Run all tests with:  nosetests -v ./tests

# Notice: Class name and method name must start with Test and test_ in order to be picked up by nose

from app.app_factory import AppFactory
from app.extensions import db
from config import TestConfig

from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager
from app.api.user_manager import UserManager
from app.models.user import User
from app.models.user import UserDetails
from app.models.room import RoomPrice
from app.models.room import Room
from app.models.booking import Booking

from datetime import datetime


class BaseDatabaseTest(object):
    '''
    Base class for testing with a dummy database.
    '''
    @classmethod
    def setup_class(cls):
        # Example: Load dummy sqlite DB
        print ("Runs before any methods in this class")
        cls.app = AppFactory.create_app(TestConfig)
        # db.init_app(cls.app)

        with cls.app.app_context():
            db.create_all()
            roomPrice = RoomPrice("single", 100, 150)
            room = Room(1, 101, 3, "Available", 1)
            booking = Booking(1, 1, datetime.strptime('2017-01-02', '%Y-%m-%d').date()
            ,datetime.strptime('2017-01-10', '%Y-%m-%d').date(), 123123123, 2000)
            RoomManager.set_availability_for_booking(datetime.strptime("2017-01-01", '%Y-%m-%d').date(), 1)
            UserManager.create_user("asd@asd.asd", "asdasd")
            user = UserManager.get_user("asd@asd.asd")
            UserManager.update_details(user, "mr", "test", "05644654")

            db.session.add(roomPrice)
            db.session.add(room)
            db.session.add(booking)
            db.session.commit()

    @classmethod
    def teardown_class(cls):
        # Example: Clear dummy DB
        print ("Runs after all methods in this class")
        with cls.app.app_context():
            db.drop_all()

    def setup(self):
        # Example: Set default values in the DB? Set up transaction?
        print ("Runs before each test method")

    def teardown(self):
        # Example: Rollback before the next test
        print ("Runs after each test method")


class TestCase(BaseDatabaseTest):
    def test_good(self):
        # An actual test
        # import modules/classes/functions and give sample input with expected output
        assert True == True
