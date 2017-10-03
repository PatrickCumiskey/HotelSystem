from flask import flash
from flask_wtf import FlaskForm as Form
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from app.api.booking_view import BookingView

class BookingForm(Form):

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

    def validate(self):
        valid = super(BookingForm, self).validate()
        if not valid:
            return False
        else:
            return True
