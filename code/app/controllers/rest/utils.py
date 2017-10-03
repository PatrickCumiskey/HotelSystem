import types
from flask import g, request, abort, jsonify, get_flashed_messages
from flask import current_app as app
from flask_httpauth import HTTPBasicAuth
from app.extensions import api
from app.auth.login import LoginManager

basic_auth = HTTPBasicAuth()


def api_route(self, *args, **kwargs):
    '''
    Class decorator for adding resources
    '''
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)


@basic_auth.verify_password
def api_verify_password(email, password):
    return LoginManager.login(email, password)


@app.route('/api/resource')
@basic_auth.login_required  # example for adding login_required
def api_get_protected_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.email})
