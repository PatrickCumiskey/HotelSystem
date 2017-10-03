import os


class BaseConfig(object):
    SECRET_KEY = os.urandom(12)


class Config(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/db_hotel'


class TestConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
