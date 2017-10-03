from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_nav import Nav

# Factories?
db = SQLAlchemy()
bootstrap = Bootstrap()
nav = Nav()
api = Api()
