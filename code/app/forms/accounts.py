from flask import flash
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, ValidationError, HiddenField, SelectField
from wtforms.validators import Required, Email, EqualTo, Length, Regexp
from app.models.role import RoleEnum, RoleFactory
import re


class ProfileForm(Form):
    user_id = HiddenField()
    first_name = StringField('First name', [Required(),
                                            Regexp('^[a-zA-z-]{2,}$',
                                                   message="Invalid first name.")])
    last_name = StringField('Last name', [Required(),
                                          Regexp('^[a-zA-z-]{2,}$',
                                                 message="Invalid last name.")])
    contact_number = StringField('Contact number',
                                 [Regexp('^((\+|00)\d{1,3}(\s)?)?\(?\d{2,3}\)?([\s.-])?\d{3}([\s.-])?\d{4}$',
                                         message="Invalid phone number.")])


class RegisterForm(Form):
    email = StringField('Email', [Required(), Email()])
    password = PasswordField(
        'Password',
        [Required(), Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$',
                            message="Password must contain at least 6 characters with upper and lower case letters and numbers.")]
    )
    password_confirmation = PasswordField(
        'Confirm Password',
        [Required(), EqualTo('password', message='Passwords must be equal')]
    )


class LoginForm(Form):
    email = StringField('email', [Required(), Email()])
    password = PasswordField('password', [Required()])

class RegisterFormStaff(Form):
    email = StringField('Email', [Required(), Email()])
    choices = [(str(t[0]), t[1].value.capitalize()) for t in enumerate(RoleEnum)][:-1]
    role = SelectField("Role: ", coerce=str, choices=choices)
    password = PasswordField('Password', [Required()])
    password_confirmation = PasswordField(
        'Confirm Password',
        [Required(), EqualTo('password', message='Passwords must be equal')]
    )

class DeleteFormStaff(Form):
    email = StringField('Email', [Required(), Email()])
