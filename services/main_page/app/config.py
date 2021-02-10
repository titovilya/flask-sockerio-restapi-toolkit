import os


class Config(object):
    DEBUG_MODE = os.environ.get('DEBUG_MODE')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "name@gmail.com"
    MAIL_PASSWORD = "password"
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    