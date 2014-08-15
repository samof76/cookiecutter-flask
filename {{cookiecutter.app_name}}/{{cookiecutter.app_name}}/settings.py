# -*- coding: utf-8 -*-
import os

os_env = os.environ

class Config(object):
    APP_NAME = '{{cookiecutter.app_name}}'
    SECRET_KEY = os_env['{{cookiecutter.app_name | upper}}_SECRET']  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    MONGODB_DB = '{0}_{1}'.format(APP_NAME, ENV)
    MONGODB_SETTINGS = {'DB': MONGODB_DB, 'HOST': 'localhost', 'PORT': 27017}
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    # Put the db file in project root
    MONGODB_DB = '{0}_{1}'.format(APP_NAME, ENV)
    MONGODB_SETTINGS = {'DB': MONGODB_DB, 'HOST': 'localhost', 'PORT': 27017}
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing
