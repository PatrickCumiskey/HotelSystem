from flask import render_template, redirect, url_for, request, session, flash
from flask import current_app as app

from app.api.user_manager import UserManager
from app.forms.checkin import CheckInForm, CheckOutForm
from app.api.checkin_manager import CheckInManager


@app.route('/checkin_and_out/checkin', methods=['GET', 'POST'])
def checkin():
    if 'booking_user_id' not in session or 'booking_credit_num' not in session:
        return redirect(url_for('checkin_form'))

    user = UserManager.get_user_by_id(session['booking_user_id'])
    credit_num = session['booking_credit_num']

    # An exit button should clear the session cookies!!!
    # del session['booking_user_id']
    # del session['booking_credit_num']

    bookings = CheckInManager.getBookings(user.details.first_name, user.details.last_name, credit_num)

    if request.method == 'POST':
        var = int(request.form['r_num'])
        CheckInManager.check_in(var)

    return render_template('checkin_and_out/AcceptCheckIn.html', bookings=bookings, user=user)


@app.route('/checkin_and_out/checkinform', methods=['GET', 'POST'])
def checkin_form():
    form = CheckInForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        credit_num = form.credit_num.data

        # This implementation (for unauthenticated users works)
        # An alternatice could be added for logged in users too
        bookings = CheckInManager.getBookings(first_name, last_name, credit_num)

        if (bookings):
            user = bookings[0].user
            session['booking_user_id'] = user.id
            session['booking_credit_num'] = credit_num
            return redirect(url_for('checkin'))
        else:
            flash('Sorry, the Name or Credit Card number is wrong or no bookings could be found\n', 'danger')

    return render_template('checkin_and_out/CheckIn.html', fm=form)


@app.route('/checkin_and_out/checkoutform', methods=['GET', 'POST'])
def checkout():
    form = CheckOutForm()
    if form.validate_on_submit():
        credit_num = form.credit_num.data

        if CheckInManager.check_out(credit_num):
            return render_template('/checkin_and_out/AcceptCheckOut.html')
        else:
            flash('Your credit card number is incorrect or you have no records to checkout', 'danger')

    return render_template('checkin_and_out/CheckOut.html', fm=form)
