import os
from flask import Flask
from .extensions import api, db, bootstrap, nav


class AppFactory(object):
    @staticmethod
    def create_app(config):
        app = Flask(__name__)
        app.config.from_object(config)
        with app.app_context():
            AppFactory._load_extensions_before(app)
            AppFactory._build_database()
            AppFactory._load_controllers(app)
            AppFactory._load_extensions_after(app)
        return app

    @staticmethod
    def _load_extensions_before(app):
        db.init_app(app)
        bootstrap.init_app(app)
        nav.init_app(app)

    @staticmethod
    def _build_database():
        # Load database schemas (ORM models)
        from app.models import user, role, room, booking, permission

        # Initialise DB
        db.create_all()

    @staticmethod
    def _load_controllers(app):
        # Load controllers/endpoints
        from app.controllers import frontend
        from app.controllers import rest

    @staticmethod
    def _load_extensions_after(app):
        api.init_app(app)
