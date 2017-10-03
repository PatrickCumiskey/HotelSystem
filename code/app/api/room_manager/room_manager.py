from app.models.room import Room
from app.models.room import RoomPrice
from app.models.room import RoomStatus
from app.api.utils import Observable
from app.api.utils import ObserverTest
from datetime import datetime
from app.extensions import db

observable = Observable()
observer_test = ObserverTest()
observable.register(observer_test)

class RoomManager(object):

    @staticmethod
    def get_room(number):
        room = Room.query.filter(Room.number == number).first()
        result = {
            'number': room.number,
            'type':room.type,
            'occupancy':room.occupancy,
            'availability':room.availability,
            'clean':room.clean,
            'weekday_price':room.room_price.price_weekday,
            'weekend_price':room.room_price.price_weekend
        }
        if not room:
            return False
        else:
            return result


    @staticmethod
    def get_room_price_from_number(number):
        room = Room.query.filter(Room.number == number).first()
        result = {
            'weekday_price':room.room_price.price_weekday,
            'weekend_price':room.room_price.price_weekend
        }
        if not room:
            return False
        else:
            return result

    @staticmethod
    def get_room_price_from_type(room_type):
        room = RoomPrice.query.filter(RoomPrice.type == room_type).first()
        if not room:
            return False
        result = {
            'weekday_price':room.price_weekday,
            'weekend_price':room.price_weekend
        }
        return result

    @staticmethod
    def get_room_clean(number):
        room = Room.query.filter(Room.number == number).first()
        if not room:
            return False
        result = {
            'Room clean status':room.clean,
        }
        return result

    @staticmethod
    def set_room_clean(number,clean):
        room = Room.query.filter(Room.number == number).first()
        if not room:
            return False
        if clean == 'True':
            clean = True
        elif clean == "False":
            clean = False
        room.clean = clean
        db.session.commit()
        return True

    @staticmethod
    def get_room_availablity(number):
        room = Room.query.filter(Room.number == number).first()
        if not room:
            return False
        result = {
            'Room availability':room.availability,
        }
        return result

    @staticmethod
    def set_room_availablity(number,availability):
        room = Room.query.filter(Room.number == number).first()
        if not room:
            return False
        room.availability = availability
        db.session.commit()
        return True


    @staticmethod
    def get_rooms_occupied_on_date(date, room_type):
        status = RoomStatus.query.filter(RoomStatus.date == datetime.strptime(date, '%Y-%m-%d').date(),
                                        RoomStatus.type == room_type).first()
        if not status:
            result = {
                'Room':room_type,
                'Occupied':0
            }
        else:
            result = {
                'Room':status.room_price.type,
                'Occupied':status.qty
            }
        return result

    '''
    Func will reduce roomstatus qty by one
    If no entry will generate a new one
    '''
    @staticmethod
    def set_availability_for_booking(date, room_type):
        booking = RoomStatus.query.filter(RoomStatus.date == date,
                                        RoomStatus.type == room_type).first()
        if not booking:
            booking = RoomStatus(date, room_type, 5)
            db.session.add(booking)
        if booking.qty > 0:
            booking.qty -=1
        if booking.qty < 3:
            observable.update_observers('Room availability low',
            Alert="Room Type: %s Number left: %s Date: %s" %(booking.room_price.type,booking.qty,booking.date))
        else:
            return False
        db.session.commit()

    '''
    Use when booking canceled
    '''
    @staticmethod
    def increase_availability_for_booking(date, room_type):
        booking = RoomStatus.query.filter(RoomStatus.date == date,
                                        RoomStatus.type == room_type).first()
        if not booking:
            return False
        booking.qty +=1
        db.session.commit()


    @staticmethod
    def pricechange(room_id,weekday_price,weekend_price):
        room_update = (RoomPrice.query.filter_by(_id=room_id).first())
        room_update._price_weekday = weekday_price
        room_update._price_weekend = weekend_price

        db.session.add(room_update)
        db.session.commit()
