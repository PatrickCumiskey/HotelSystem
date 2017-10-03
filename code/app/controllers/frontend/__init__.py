from flask import g, request, session, render_template, flash, redirect, url_for
from flask import current_app as app

from app.auth.login import LoginManager, login_required
from app.auth.access import user_is, user_can

from app.controllers.frontend import navigation
from app.controllers.frontend import accounts
from app.controllers.frontend import error
from app.controllers.frontend import test
from app.controllers.frontend import booking
from app.controllers.frontend import rooms
from app.controllers.frontend import checkin_and_out
from app.controllers.frontend import staff




@app.route('/')
def home():
    text = ''
    if not LoginManager.is_logged_in():
        text = "Hello!  <a href='/accounts/login'>Login</a>"
    else:
        text = "Hello "+g.user.email+"!  <a href='/accounts/logout'>Logout</a>"
    return render_template('layout.html', text=text)

@app.before_request
def load_user():
    LoginManager.load_user()
