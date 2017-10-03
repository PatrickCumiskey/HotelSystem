# 11. Contribution

The following bash scripts were used to generate the output:

~~~BASH
for file in $(git ls-files | grep code | grep -Ev "__init__.py|*.md"); do
    git blame --line-porcelain $file | cat;
done\
| grep  "^author "|sort|uniq -c
~~~

~~~BASH
for file in $(git ls-files | grep code | grep -Ev "__init__.py|*.md|*.html|*.css"); do
    echo '\n';
    echo $file;
    echo '==============================================';

    classes=$(awk '/^class/ {print "     " $2}' $file)
    if [ $classes ]; then
    	echo ' Classes:'
    	echo $classes
    fi

    func=$(awk '/^def/ {print "     " $2}' $file)
    if [ $func ]; then
    	echo ' Functions:'
    	echo $func
    fi

    echo ' Contribution in lines:'
    git blame --line-porcelain $file | cat | grep  "^author "|sort|uniq -c;
done
~~~

### Lines of Code per Team Member:
~~~
 128 author EasternBob
 823 author JonneyLloyd
1257 author OliverGavin
 572 author Patrick Cumiskey
----
2780 Total
~~~

### Packages, Classes & Functions, Authors, Lines of Code (excluding html):
~~~
code/app/api/booking_manager/manage_bookings.py
==============================================
 Classes:
     makeBooking(object):
     cancelBooking(object):
 Contribution in lines:
    140 author Patrick Cumiskey


code/app/api/booking_view/booking_view.py
==============================================
 Classes:
     BookingView(object):
 Contribution in lines:
     12 author EasternBob
     83 author JonneyLloyd
      1 author OliverGavin
      2 author Patrick Cumiskey


code/app/api/checkin_manager/checkin_manager.py
==============================================
 Classes:
     CheckInManager(object):
 Contribution in lines:
     41 author OliverGavin


code/app/api/room_manager/room_manager.py
==============================================
 Classes:
     RoomManager(object):
 Contribution in lines:
    144 author JonneyLloyd
     13 author Patrick Cumiskey


code/app/api/user_manager/user_manager.py
==============================================
 Classes:
     UserManager(object):
 Contribution in lines:
     48 author OliverGavin
     10 author Patrick Cumiskey


code/app/api/utils/observable.py
==============================================
 Classes:
     Observable(object):
 Contribution in lines:
     20 author JonneyLloyd


code/app/api/utils/observer.py
==============================================
 Classes:
     Observer(object):
 Contribution in lines:
      8 author JonneyLloyd


code/app/api/utils/observer_test.py
==============================================
 Classes:
     ObserverTest(object):
 Contribution in lines:
      1 author EasternBob
      3 author JonneyLloyd


code/app/app_factory.py
==============================================
 Classes:
     AppFactory(object):
 Contribution in lines:
     40 author OliverGavin


code/app/auth/access/access.py
==============================================
 Classes:
     AccessManager(object):
 Contribution in lines:
     61 author OliverGavin


code/app/auth/access/decorators.py
==============================================
 Functions:
     user_is(*roles):
     user_can(*permissions):
 Contribution in lines:
     66 author OliverGavin


code/app/auth/access/exceptions.py
==============================================
 Classes:
     UserIsNotPermitted(Exception):
 Contribution in lines:
      2 author OliverGavin


code/app/auth/login/decorators.py
==============================================
 Functions:
     login_required(f):
 Contribution in lines:
     23 author OliverGavin


code/app/auth/login/exceptions.py
==============================================
 Classes:
     UserIsNotAuthorized(Exception):
 Contribution in lines:
      2 author OliverGavin


code/app/auth/login/login.py
==============================================
 Classes:
     LoginManager(object):
 Contribution in lines:
     44 author OliverGavin


code/app/controllers/frontend/accounts.py
==============================================
 Functions:
     profile():
     edit_profile():
     register():
     login():
     logout():
 Contribution in lines:
    104 author OliverGavin


code/app/controllers/frontend/booking.py
==============================================
 Functions:
     booking():
     booking_view():
     result():
     make_book_form():
     cancel_booking_form():
     make_book():
     cancel_booking():
     change_price_form():
     change_price():
 Contribution in lines:
     15 author JonneyLloyd
    102 author Patrick Cumiskey


code/app/controllers/frontend/checkin_and_out.py
==============================================
 Functions:
     checkin():
     checkin_form():
     checkout():
 Contribution in lines:
     15 author EasternBob
     49 author OliverGavin


code/app/controllers/frontend/error.py
==============================================
 Functions:
     user_not_authorised(error):
     user_not_permitted(error):
     page_not_found(error):
 Contribution in lines:
     20 author OliverGavin


code/app/controllers/frontend/navigation.py
==============================================
 Functions:
     navbar():
 Contribution in lines:
     23 author OliverGavin
     11 author Patrick Cumiskey


code/app/controllers/frontend/rooms.py
==============================================
 Functions:
     rooms():
     room_clean():
 Contribution in lines:
     30 author JonneyLloyd


code/app/controllers/frontend/staff.py
==============================================
 Functions:
     add_staff_form():
     remove_staff_form():
 Contribution in lines:
     40 author Patrick Cumiskey


code/app/controllers/frontend/test.py
==============================================
 Functions:
     special():
     special_admin():
     special_guest():
 Contribution in lines:
     25 author OliverGavin


code/app/controllers/rest/accounts.py
==============================================
 Classes:
     AccountListAPI(Resource):
     AccountAPI(Resource):
 Contribution in lines:
     60 author OliverGavin


code/app/controllers/rest/utils.py
==============================================
 Functions:
     api_route(self,
     api_verify_password(email,
     api_get_protected_resource():
 Contribution in lines:
     31 author OliverGavin


code/app/extensions.py
==============================================
 Contribution in lines:
     10 author OliverGavin


code/app/forms/accounts.py
==============================================
 Classes:
     ProfileForm(Form):
     RegisterForm(Form):
     LoginForm(Form):
     RegisterFormStaff(Form):
     DeleteFormStaff(Form):
 Contribution in lines:
     24 author OliverGavin
     16 author Patrick Cumiskey


code/app/forms/booking.py
==============================================
 Classes:
     BookingForm(Form):
 Contribution in lines:
     17 author JonneyLloyd


code/app/forms/checkin.py
==============================================
 Classes:
     CheckInForm(Form):
     CheckOutForm(Form):
 Contribution in lines:
      9 author EasternBob
      4 author OliverGavin


code/app/forms/rooms.py
==============================================
 Classes:
     RoomAvailabilityForm(Form):
     SetRoomCleanForm(Form):
 Contribution in lines:
     43 author JonneyLloyd


code/app/models/booking/booking.py
==============================================
 Classes:
     Booking(db.Model):
 Contribution in lines:
      6 author EasternBob
     57 author JonneyLloyd
     43 author OliverGavin


code/app/models/permission/factory.py
==============================================
 Classes:
     PermissionFactory(object):
 Contribution in lines:
     18 author OliverGavin


code/app/models/permission/permission.py
==============================================
 Classes:
     PermissionEnum(Enum):
     Permission(db.Model):
 Contribution in lines:
     57 author OliverGavin


code/app/models/role/factory.py
==============================================
 Classes:
     RoleFactory(object):
 Contribution in lines:
     41 author OliverGavin


code/app/models/role/role.py
==============================================
 Classes:
     RoleEnum(Enum):
     Role(db.Model):
 Contribution in lines:
     66 author OliverGavin


code/app/models/room/room.py
==============================================
 Classes:
     Room(db.Model):
 Contribution in lines:
      5 author EasternBob
     47 author JonneyLloyd
     28 author OliverGavin


code/app/models/room/room_price.py
==============================================
 Classes:
     RoomPrice(db.Model):
 Contribution in lines:
     27 author JonneyLloyd
     24 author OliverGavin


code/app/models/room/room_status.py
==============================================
 Classes:
     RoomStatus(db.Model):
 Contribution in lines:
     56 author JonneyLloyd


code/app/models/user/user.py
==============================================
 Classes:
     User(db.Model):
 Contribution in lines:
      8 author JonneyLloyd
     63 author OliverGavin


code/app/models/user/user_details.py
==============================================
 Classes:
     UserDetails(db.Model):
 Contribution in lines:
      3 author EasternBob
     24 author JonneyLloyd
     22 author OliverGavin


code/config.py
==============================================
 Classes:
     BaseConfig(object):
     Config(BaseConfig):
     TestConfig(BaseConfig):
 Contribution in lines:
     15 author OliverGavin


code/requirements.txt
==============================================
 Contribution in lines:
     10 author OliverGavin


code/server.py
==============================================
 Contribution in lines:
      6 author OliverGavin


code/tests/booking_manager_tests.py
==============================================
 Classes:
     TestBookingManger(BaseDatabaseTest):
 Contribution in lines:
     66 author Patrick Cumiskey


code/tests/booking_tests.py
==============================================
 Classes:
     AnObserver(Observer):
     TestBookingView(BaseDatabaseTest):
 Contribution in lines:
    121 author JonneyLloyd
      4 author JonneyLLoyd


code/tests/test.py
==============================================
 Classes:
     BaseDatabaseTest(object):
     TestCase(BaseDatabaseTest):
 Contribution in lines:
     24 author JonneyLLoyd
     45 author OliverGavin
~~~
