from flask import g, render_template, redirect, url_for, request, session, flash
from flask import current_app as app
from app.extensions import db
from app.api.booking_view import BookingView
from app.api.user_manager import UserManager
from app.forms.booking import BookingForm
from flask import render_template, redirect, url_for, request, session
from app.api.booking_manager import cancelBooking, makeBooking
from app.models.room import Room, RoomPrice
from app.models.user import User
from app.auth.login import LoginManager, login_required
from app.auth.access import user_is, user_can
from app.forms.accounts import LoginForm, RegisterForm, ProfileForm, RegisterFormStaff, DeleteFormStaff
from app.models.role import RoleEnum, RoleFactory
import datetime


@app.route('/staff/add_staff', methods=['GET', 'POST'])
@login_required
@user_is('ADMIN')
def add_staff():
    form = RegisterFormStaff()
    if form.validate_on_submit():
        role = int(form.role.data)
        role = list(RoleEnum)[role]
        UserManager.create_user(form.email.data, form.password.data, role)
        flash(form.email.data + ' Has been added to users with role: ' + form.role.data)

    return render_template('staff/add_staff.html', form=form)


@app.route('/staff/remove_staff', methods=['GET', 'POST'])
@login_required
@user_is('ADMIN')
def remove_staff():

    form = DeleteFormStaff()
    if form.validate_on_submit():
        UserManager.remove_staff(form.email.data)
        flash(form.email.data + ' Has been added removed from users ')
    return render_template('staff/remove_staff.html', form=form)
