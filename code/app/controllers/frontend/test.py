# module for test routes before refactoring to other modules
from flask import g, request, session, render_template, flash, redirect, url_for
from flask import current_app as app

from app.auth.login import login_required
from app.auth.access import user_is, user_can


@app.route("/private/special")
@login_required
def special():
    return 'So special... you must log in!'


@app.route("/private/admin")
@login_required
@user_is('ADMIN')
def special_admin():
    return 'Admin page'


@app.route("/private/guest")
@user_is('GUEST')
def special_guest():
    return 'Guest page'
