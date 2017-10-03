from app.extensions import nav
from flask_nav.elements import Navbar, View, Subgroup, Separator, Link, Text


@nav.navigation()
def navbar():
    return Navbar(
        'Ryan Ground Hotel',
        View('Home', 'home'),
        View('Register', 'register'),
        View('Log in', 'login'),
        View('Log out', 'logout'),
        View('Profile', 'profile'),
        View('Check in', 'checkin'),
        View('Check out', 'checkout'),
        Subgroup(
            'Staff',
            View('Add Staff', 'add_staff'),
            View('Remove Staff', 'remove_staff'),
        ),
        Subgroup(
            'Bookings',
            View('View Bookings', 'booking'),
            View('Make a Booking', 'make_book_form'),
            View('Cancel', 'cancel_booking_form'),
            View('Price', 'change_price_form'),
        ),
        Subgroup(
            'Test',
            View('admin role', 'special_admin'),
            View('guest role', 'special_guest'),
            Separator(),
            Text('Testing'),
            View('Login required', 'special'),
        ),
    )
