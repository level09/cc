# -*- coding: utf-8 -*-
import os

os_env = os.environ

class Config(object):
    SECRET_KEY = '3nF3Rn0'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    BROKER_URL = 'redis://localhost:6379/10'
    MONGODB_SETTINGS = {
        'DB': 'enferno'
    }

    #security
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = '3nF3Rn0'

    SECURITY_POST_LOGIN_VIEW = '/account'
    SECURITY_POST_CONFIRM_VIEW = '/account'


    #flask mail settings - Mailgun
    MAIL_SERVER = 'smtp.mailgun.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'user'
    MAIL_PASSWORD = 'pass'
    SECURITY_EMAIL_SENDER = 'info@level09.com'

    UPLOAD_DIR = os.path.join(os.path.dirname(__file__),'static','uploads')

    ZENCODER_KEY = '6c6319487b8884587dd84d7bff5bdc42'

    #s3 upload settings
    S3_LOCATION = 'http://net.alarabiya.merger.amazonaws.com/'
    S3_KEY = 'AKIAIT7YFXLNW7VKV2JA'
    S3_SECRET = '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'
    S3_UPLOAD_DIRECTORY = ''
    S3_BUCKET = 'net.alarabiya.merger'


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


