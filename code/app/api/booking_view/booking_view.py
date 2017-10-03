from app.models.user import User
from app.models.booking import Booking
from datetime import datetime

class BookingView(object):

    @staticmethod
    def get_booking_for_user(user_id):
        bookings = Booking.query.filter_by(user_id=user_id).all()
        result = []
        if not bookings:
            return False
        for booking in bookings:
            info = {
                'room_id': booking.room_id,
                'start_date': booking.start_date,
                'end_date': booking.end_date,
                'booking_price': booking.booking_price,
                'first_name': booking.user.details.first_name,
                'last_name': booking.user.details.last_name
            }
            result.append(info)
        return result

    @staticmethod
    def get_booking_by_credit_card(credit_card):
        bookings = Booking.query.filter_by(credit_card=credit_card).all()
        result = []
        if not bookings:
            return False
        for booking in bookings:
            info = {
                'room_id': booking.room_id,
                'start_date': booking.start_date,
                'end_date': booking.end_date,
                'booking_price': booking.booking_price,
                'first_name': booking.user.details.first_name,
                'last_name': booking.user.details.last_name
            }
            result.append(info)
        return result

    @staticmethod
    def get_booking_on_date(date):
        result = []
        bookings = Booking.query.filter(Booking.start_date <= datetime.strptime(date, '%Y-%m-%d').date(),
                                        Booking.end_date >= datetime.strptime(date, '%Y-%m-%d').date()).all()
        if not bookings:
            return False
        for booking in bookings:
            info = {
                'room_id': booking.room_id,
                'start_date': booking.start_date,
                'end_date': booking.end_date,
                'booking_price': booking.booking_price,
                'first_name': booking.user.details.first_name,
                'last_name': booking.user.details.last_name
            }
            result.append(info)
        return result

    @staticmethod
    def get_booking_between_dates(start_date, end_date):
        result = []
        bookings = Booking.query.filter(Booking.start_date >= datetime.strptime(start_date, '%Y-%m-%d').date(),
                                        Booking.start_date <= datetime.strptime(end_date, '%Y-%m-%d').date()).all()
        if not bookings:
            return False
        for booking in bookings:
            info = {
                'room_id': booking.room_id,
                'start_date': booking.start_date,
                'end_date': booking.end_date,
                'booking_price': booking.booking_price,
                'first_name': booking.user.details.first_name,
                'last_name': booking.user.details.last_name
            }
            result.append(info)
        return result
    '''
    TODO will need to impliment a daily price table
    to make this and forecasting more accurate
    '''
    @staticmethod
    def get_sales_between_dates(start_date, end_date):
        bookings = Booking.query.filter(Booking.start_date >= datetime.strptime(start_date, '%Y-%m-%d').date(),
                                        Booking.start_date <= datetime.strptime(end_date, '%Y-%m-%d').date()).all()
        if not bookings:
            return False
        result = []
        total = 0.0;
        for booking in bookings:
            info = {
                'room_id': booking.room_id,
                'date': booking.start_date,
                'booking_price': booking.booking_price,
                'first_name': booking.user.details.first_name,
                'last_name': booking.user.details.last_name
            }
            result.append(info)
            total = total + booking.booking_price
        total_ret = {'total': total}
        result.append(total_ret)
        return result
