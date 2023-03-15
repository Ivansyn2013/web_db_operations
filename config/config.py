import os

from dotenv import load_dotenv, dotenv_values

class Config(object):
    TESTING = False
    WTF_CSRF_ENABLED = True


class DeployConfig(Config):
    load_dotenv()
    config = os.environ
    SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_MODIFICATIONS = config['SQLALCHEMY_MODIFICATIONS']
    SECRET_KEY = config['SECRET_KEY']
    POSTGRES_DB = config['POSTGRES_DB']
    POSTGRES_USER = config['POSTGRES_USER']
    POSTGRES_PASSWORD = config['POSTGRES_PASSWORD']
    PGDATA = config['PGDATA']

class DeveloperPostgresConfig(Config):
    config = dotenv_values('.env')
    TESTING = True
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_MODIFICATIONS = config['SQLALCHEMY_MODIFICATIONS']
    SECRET_KEY = config['SECRET_KEY']
    POSTGRES_DB = config['POSTGRES_DB']
    POSTGRES_USER = config['POSTGRES_USER']
    POSTGRES_PASSWORD = config['POSTGRES_PASSWORD']
    PGDATA = config['PGDATA']