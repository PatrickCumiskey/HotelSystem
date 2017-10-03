from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required


class CheckInForm(Form):
    first_name = StringField('Firstname', [Required()])
    last_name = StringField('Lastname', [Required()])
    credit_num = IntegerField('Credit', [Required()])


class CheckOutForm(Form):
    credit_num = StringField('CreditNum', [Required()])
