from flask import g, request, session, render_template, flash, redirect, url_for, abort
from flask import current_app as app

from app.auth.login import LoginManager, login_required
from app.auth.access import user_is, user_can, AccessManager
from app.forms.accounts import LoginForm, RegisterForm, ProfileForm

from app.api.user_manager import UserManager

from app.models.permission import PermissionEnum as P
from app.models.role import RoleEnum as R


@app.route('/accounts/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user_id = request.args.get('id')
    if user_id is not None:
        user = UserManager.get_user_by_id(user_id)
    else:
        user = g.user

    if user is None:
        abort(404)

    AccessManager.check_user_has_permission_on(user, P.VIEW_OTHER_USER, P.VIEW_USER)
    return render_template('accounts/profile.html', user=user)


@app.route('/accounts/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = ProfileForm()

    if form.validate_on_submit():
        user = UserManager.get_user_by_id(form.user_id.data)

        if user is None:
            abort(404)

        AccessManager.check_user_has_permission_on(user, P.VIEW_OTHER_USER, P.VIEW_USER)
        UserManager.update_details(user, form.first_name.data, form.last_name.data, form.contact_number.data)
        return redirect(url_for('profile', id=user.id))

    else:
        user_id = request.args.get('id')
        if user_id is not None:
            user = UserManager.get_user_by_id(user_id)
        else:
            user = g.user

        if user is None:
            abort(404)

        AccessManager.check_user_has_permission_on(user, P.VIEW_OTHER_USER, P.VIEW_USER)

        form.user_id.data = user.id
        if not form.is_submitted() and user.details is not None:
            form.first_name.data = user.details.first_name
            form.last_name.data = user.details.last_name
            form.contact_number.data = user.details.contact_number

    return render_template('accounts/edit-profile.html', form=form)


@app.route('/accounts/register', methods=['GET', 'POST'])
@user_is(R.ANONYMOUS)
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        if not UserManager.create_user(form.email.data, form.password.data):
            flash('This email is already in use.', 'danger')
        else:
            LoginManager.login(form.email.data, form.password.data)
            return redirect(url_for('edit_profile'))

    return render_template('accounts/register.html', form=form)


@app.route('/accounts/login', methods=['GET', 'POST'])
@user_is(R.ANONYMOUS)
def login():
    form = LoginForm()
    if form.validate_on_submit():

        if not LoginManager.login(form.email.data, form.password.data):
            flash('Incorrect email or password. Please try again.', 'danger')
        else:
            return redirect(url_for('home'))

    return render_template('accounts/login.html', form=form)


@app.route("/accounts/logout")
def logout():
    LoginManager.logout()
    return redirect(url_for('home'))
