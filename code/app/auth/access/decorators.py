import functools

from .access import AccessManager
from .exceptions import UserIsNotPermitted


def user_is(*roles):
    '''
    Creates a decorator to verify a user has ANY of the provided roles.

    Examples:
    @user_is(['AGENT', 'GUEST'])
    def book_room():
        print('Either role required')

    Args:
        In:
            f (function):   The function to decorate
            permission (str|list(str)): The required role

        Out:
            function:   Decorated function
    '''
    def decorator(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            if not any(AccessManager.user_is_role(r) for r in roles):
                raise UserIsNotPermitted
            return f(*args, **kwargs)
        return decorated
    return decorator


def user_can(*permissions):
    '''
    Creates a decorator to verify a user has ANY of the provided permissions.
    To verify that a user has combinations of permissions; repeat
    the decorator.

    Examples:
    @user_can(['MAKE_BOOKING', 'MAKE_BOOKING_OTHER'])
    def book_room():
        print('Either permission required')

    @user_can('MAKE_COMPANY_BOOKING')
    @user_can(['MAKE_BOOKING', 'MAKE_BOOKING_OTHER'])
    def book_company():
        print('The user can make comany bookings and either other
              permission required')

    Args:
        In:
            f (function):   The function to decorate
            permission (str|list(str)): The required permission

        Out:
            function:   Decorated function
    '''
    def decorator(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            if not any(AccessManager.user_has_permission(p) for p in permissions):
                raise UserIsNotPermitted
            return f(*args, **kwargs)
        return decorated
    return decorator
