from flask import g, request, abort, jsonify, get_flashed_messages
from flask_restful import Resource
from app.extensions import api

from app.auth.login import LoginManager, login_required
from app.auth.access import user_is, user_can
from app.forms.accounts import LoginForm, RegisterForm

from app.api.user_manager import UserManager

from .utils import basic_auth


@api.route('/api/v1.0/accounts')
class AccountListAPI(Resource):
    '''
    Example test on linux (a unit test would be better):
        curl -i -X POST -H "Content-Type: application/json" -d '{"email":"tester@gmail.com","password":"python"}' http://127.0.0.1:5000/api/v1.0/accounts
    '''
    # decorators = [basic_auth.login_required]
    # decorators = [user_is('ADMIN')]

    # @user_is('ADMIN')
    def get(self):
        '''
        Retrieve list of users
        '''
        pass

    def post(self):
        '''
        Create a new user
        '''
        data = request.get_json()
        data['password_confirmation'] = data['password']
        form = RegisterForm(data=data, csrf_enabled=False)
        if form.validate():

            if not UserManager.create_user(form.email.data, form.password.data):
                return {'form_errors': 'This email is already in use.'}, 400
            else:
                return {'email': form.email.data}, 201  # TODO: return a dictionary pointing to the newly created resource
                    # {'Location': url_for('get_user', id = user.id, _external = True)}     # Suggest location of next request
        else:
            return {'form_field_errors': form.errors}, 400


@api.route('/api/v1.0/accounts/<int:id>')
class AccountAPI(Resource):
    def get(self, id):
        '''
        Retrieve a user
        '''
        pass

    def put(self, id):
        '''
        Update an existing user
        '''
        pass
