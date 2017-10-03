from flask import render_template, redirect, url_for
from flask import current_app as app

from app.auth.login import UserIsNotAuthorized
from app.auth.access import UserIsNotPermitted


@app.errorhandler(UserIsNotAuthorized)
def user_not_authorised(error):
    return render_template('layout.html', text='Unauthorised access. Please log in.'), 403


@app.errorhandler(UserIsNotPermitted)
def user_not_permitted(error):
    return render_template('layout.html', text='Permission denied.'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('layout.html', text='This page does not exist'), 404
