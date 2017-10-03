from flask import flash
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, ValidationError, IntegerField, RadioField
from wtforms.validators import Required, EqualTo
from app.api.room_manager import RoomManager

class RoomAvailabilityForm(Form):
    date = StringField('Date', [Required()])
    room_type = StringField('Room Type', [Required()])
    def __init__(self, *args, **kwargs):
        super(RoomAvailabilityForm, self).__init__(*args, **kwargs)
    def validate(self):
        valid = super(RoomAvailabilityForm, self).validate()
        if not valid:
            return False
        date = self.date.data
        room_type = self.room_type.data
        if not RoomManager.get_rooms_occupied_on_date(date, room_type):
            flash('Error', 'danger')
            return False
        else:
            return True

class SetRoomCleanForm(Form):
    number = IntegerField('Room No.', [Required()])
    clean = RadioField('Clean',  choices=[('True','Clean'),('False','Unclean')],
                        default='Clean', validators=[Required()])
    available = RadioField('Available',  choices=[('Available','Available'),('Not Ready','Not Ready'), ('Occupied','Occupied')],
                        default='Available', validators=[Required()])
    def __init__(self, *args, **kwargs):
        super(SetRoomCleanForm, self).__init__(*args, **kwargs)
    def validate(self):
        valid = super(SetRoomCleanForm, self).validate()
        if not valid:
            return False
        number = self.number.data
        clean = self.clean.data
        available = self.available.data
        if not RoomManager.set_room_clean(number, clean) or not RoomManager.set_room_availablity(number, available):
            flash('Error', 'danger')
            return False
        else:
            return True
