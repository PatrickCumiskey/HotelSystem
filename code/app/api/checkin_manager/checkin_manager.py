from app.extensions import db
from app.models.booking import Booking
from app.models.user.user_details import UserDetails
from app.models.user import User
from app.models.room import Room
from app.models.room.room_price import RoomPrice
from app.models.role.role import Role


class CheckInManager(object):
    @staticmethod
    def getBookings(first_name, last_name, credit_num):
        bookings = db.session.query(Booking).filter(UserDetails.id == User.id,
                                                    Booking.user_id == User.id,
                                                    UserDetails.first_name == first_name,
                                                    UserDetails.last_name == last_name,
                                                    Booking.credit_card == credit_num)
        if(bookings.first() is None):
            return []
        else:
            return bookings.all()

    @staticmethod
    def check_in(room_num):
        rooms = db.session.query(Room).filter(Room.number == room_num).all()
        for m in rooms:
            m.availability = 'N'
        db.session.commit()

    @staticmethod
    def check_out(creditnum):
        # This does check out the user... but it does not prevent them from checking in again!!
        rooms = db.session.query(Room).filter(Booking.credit_card == creditnum, Booking.room_id == Room.id)
        if rooms.first() is None:
            return False
        else:
            for m in rooms.all():
                m.clean = 1
                m.availability = 'Y'
            db.session.commit()
            return True
