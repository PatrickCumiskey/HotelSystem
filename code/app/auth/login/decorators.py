import functools

from .login import LoginManager
from .exceptions import UserIsNotAuthorized


def login_required(f):
    '''
    Decorator to verify a user is logged in.

    Args:
        In:
            f (function):   The function to decorate

        Out:
            function:   Decorated function
    '''
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        if not LoginManager.is_logged_in():
            raise UserIsNotAuthorized
        return f(*args, **kwargs)
    return decorated
