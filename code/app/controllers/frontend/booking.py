from flask import g, render_template, redirect, url_for, request, session, flash
from flask import current_app as app
from app.extensions import db
from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager
from app.forms.booking import BookingForm
from flask import render_template, redirect, url_for, request, session
from app.api.booking_manager import cancelBooking, makeBooking
from app.models.room import Room,RoomPrice
from app.models.booking import Booking
from app.auth.login import LoginManager,login_required
from app.auth.access import user_is, user_can
import datetime

@app.route('/booking/booking', methods=['GET', 'POST'])
@login_required
def booking():
    form = BookingForm()
    if form.validate_on_submit():
        result = BookingView.get_booking_for_user(g.user.id)
        if result:
            return render_template("booking/bookingView.html", result=result)


    return render_template('booking/bookingForm.html', form=form)


@app.route('/accounts/make-book-form', methods=['GET', 'POST'])
@login_required
def make_book_form():

    room_list = makeBooking.get_existing_rooms()

    return render_template('booking/makebooking.html', room_list = room_list)


@app.route('/booking/cancelbookform', methods=['GET', 'POST'])
@login_required
def cancel_booking_form():
    user_id = g.user.id
    customer_bookings = Booking.query.filter_by(user_id = user_id).all()

    bookings_start = [book.start_date for book in customer_bookings]
    bookings_room = [book.room_id for book in customer_bookings]



    return render_template('booking/cancelBooking.html', bookings_start = bookings_start,bookings_room =bookings_room )


@app.route('/accounts/makebooking', methods=['GET', 'POST'])
@login_required
def make_book():
    if request.method == 'POST':
        room_id = request.form['room_type']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        credit_card = request.form['credit_card']

    user_id = g.user.id
    success = False
    if credit_card != "" and start_date != "" and end_date != "" and room_id != "":
        success = makeBooking.bookingmake(user_id, room_id, start_date, end_date, credit_card)
    if (success):
        return render_template('booking/bookingSuccess.html')
    else:
        return render_template('booking/bookingFailed.html')


@app.route('/accounts/cancelbook', methods=['GET', 'POST'])
@login_required
def cancel_booking():
    credit_card = request.form['credit_card']
    booked_room_number = request.form['booked_room_number']
    booked_start_date = request.form['booked_start_date']

    user_id = g.user.id
    canceled = cancelBooking.bookingcancel(user_id,credit_card, booked_room_number, booked_start_date)
    if (canceled):
        return render_template('booking/roomCanceled.html')
    else:
        return render_template('booking/roomCancelFail.html')


@app.route('/booking/changepriceform', methods=['GET', 'POST'])
@user_is('ADMIN')
def change_price_form():
    room_list = makeBooking.get_existing_rooms()

    return render_template('booking/changeprice.html', room_list=room_list)


@app.route('/accounts/changeprice', methods=['GET', 'POST'])
def change_price():
    if request.method == 'POST':
        room_id = request.form['room_id']
        weekday_price = request.form['weekday_price']
        weekend_price = request.form['weekend_price']
        RoomManager.pricechange(room_id,weekday_price,weekend_price)

    return render_template('booking/priceChanged.html')
