from app.models.room import Room
from app.models.room import RoomPrice
from app.extensions import db
from app.models.booking import Booking
from app.api.room_manager import RoomManager
from app.models.room import RoomStatus
from datetime import datetime, date, timedelta
import datetime


class makeBooking(object):
    @staticmethod
    def bookingmake(user_id, room_type, start_date, end_date, credit_card):

        new_start = start_date.replace('-', "")
        new_end = end_date.replace('-', "")
        date_start = datetime.datetime.strptime(new_start, '%Y%m%d').date()
        date_end = datetime.datetime.strptime(new_end, '%Y%m%d').date()

        if date_start < datetime.datetime.now().date() or date_end < datetime.datetime.now().date():
            return False

        distance = date_end - date_start
        distance = distance.days

        base = date_start
        date_list = [base + datetime.timedelta(days=x) for x in range(0, distance)]

        total_price = 0

        room_type_number = int(room_type)

        for date_booked in date_list:
            result = RoomManager.set_availability_for_booking(date_booked, room_type_number)
            if result == False:
                return False

        # Get total price of room
        room_wanted = (RoomPrice.query.filter_by(_id=room_type).first())
        room_number_object = (Room.query.filter_by(_type=room_type).all())
        room_found = False

        for room_available in room_number_object:
            room_number = room_available.id

            room_bookings = (Booking.query.filter_by(_room_id=room_number).all())

            if (room_bookings != [] and not room_found):

                for room_date in room_bookings:

                    room_date_start = room_date._start_date
                    room_date_end = room_date._end_date
                    if (date_start <= room_date_start and date_end >= room_date_end or date_start >= room_date_start
                    and date_end <= room_date_end and room_number == room_date._room_id):

                        break
                    else:

                        room_to_book = room_available
                        room_found = True
                        break

            else:
                room_to_book = (Room.query.filter_by(id=room_number).first())

        try:
            room_number = room_to_book.id
            weekday_price = room_wanted._price_weekday
            weekend_price = room_wanted._price_weekend
            for i in range(0, distance):
                day_booked = (date_start + timedelta(days=i))
                # gets day as an integer 0 being monday and 6 being sunday
                start_day = day_booked.weekday()

                # is it a weekday?
                date = date_list[i]

                booking = RoomStatus.query.filter(RoomStatus.date == date,
                                                  RoomStatus.type == room_type).first()

                if (start_day < 5 and booking.qty >= 19):
                    total_price += weekday_price
                elif (start_day < 5 and booking.qty < 19):
                    total_price += weekday_price * 2
                # if not, is weekend
                elif (start_day > 5 and booking.qty >= 19):
                    total_price += weekend_price
                else:
                    total_price += weekend_price * 2



            start_dated = datetime.datetime.strptime(new_start, '%Y%m%d').date()
            end_dated = datetime.datetime.strptime(new_end, '%Y%m%d').date()

            room_booking = Booking(user_id, room_number, start_dated, end_dated, credit_card, total_price)

            db.session.add(room_booking)
            db.session.commit()
            return True
        except (NameError,AttributeError):

            return False

    def get_existing_rooms():

        room_list2 = []

        for value in db.session.query(Room.type).distinct():
            name = RoomPrice.query.filter_by(id=value[0]).first()
            room_list2.append(name)

        return room_list2

class cancelBooking(object):
    @staticmethod
    def bookingcancel(user_id, credit_card, booked_room_number, booked_start_date):
        booked_start_date = booked_start_date.replace('-', "")
        booked_start_date = datetime.datetime.strptime(booked_start_date, '%Y%m%d').date()
        booking_instance = Booking.query.filter_by(user_id = user_id,credit_card=credit_card, _room_id=booked_room_number,
                                                   _start_date=booked_start_date).first()

        if (booking_instance):
            room_type_obj = Room.query.filter_by(_id=booked_room_number).first()

            room_type = room_type_obj.type

            date_start = booking_instance._start_date
            date_end = booking_instance._end_date

            distance = date_end - date_start
            distance = distance.days

            base = date_start
            date_list = [base + datetime.timedelta(days=x) for x in range(0, distance)]

            for date_booked in date_list:
                RoomManager.increase_availability_for_booking(date_booked, room_type)

            Booking.query.filter_by(user_id=user_id, credit_card=credit_card, _room_id=booked_room_number,
                                    _start_date=booked_start_date).delete()
            db.session.commit()
            return True
        else:
            return False
