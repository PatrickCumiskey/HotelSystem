from flask import render_template, redirect, url_for, request, session
from flask import current_app as app

from app.auth.login import LoginManager, login_required
from app.api.room_manager import RoomManager
from app.forms.rooms import RoomAvailabilityForm
from app.forms.rooms import SetRoomCleanForm

@app.route('/rooms/rooms', methods=['GET', 'POST'])
@login_required
def rooms():
    form = RoomAvailabilityForm()
    if form.validate_on_submit():
        result = RoomManager.get_rooms_occupied_on_date(date=form.date.data, room_type=form.room_type.data)
        return render_template("rooms/roomview.html",result = result)

    return render_template('rooms/rooms.html', form=form)

@app.route('/rooms/room-clean', methods=['GET', 'POST'])
@login_required
def room_clean():
    form = SetRoomCleanForm()
    if form.validate_on_submit():
        clean_result = RoomManager.set_room_clean(number=form.number.data, clean=form.clean.data)
        available_result = RoomManager.set_room_availablity(number=form.number.data, availability=form.available.data)
        if clean_result and available_result:
            result = RoomManager.get_room(number=form.number.data)
            return render_template("rooms/roomview.html",result = result)

    return render_template('rooms/room-clean.html', form=form)
