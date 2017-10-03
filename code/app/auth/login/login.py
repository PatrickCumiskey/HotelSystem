from flask import g, session
from app.extensions import db
from app.models.user import User
from app.models.role import RoleEnum, RoleFactory

from app.api.user_manager import UserManager


class LoginManager(object):

    @staticmethod
    def login(email, password):
        user = UserManager.get_user(email)

        if not user or not user.verify_password(password):
            return False

        session['logged_in'] = True
        session['user_id'] = user.id
        g.user = user
        return True

    @staticmethod
    def logout():
        session['logged_in'] = False
        session.pop('user_id', None)

    @staticmethod
    def load_user():
        if "user_id" in session:
            user = UserManager.get_user_by_id(id=session["user_id"])
            session['logged_in'] = True
        else:
            user = UserManager.get_anonymous_user()
            session['logged_in'] = False
        g.user = user

    @staticmethod
    def get_current_user():
        return g.user

    @staticmethod
    def is_logged_in():
        return session['logged_in']
