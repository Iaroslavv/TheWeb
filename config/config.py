import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_ECHO = False
SECRET_KEY = "1bghg3hg4ufa58ghf57gh"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = "iaroslavmusic@gmail.com"
MAIL_PASSWORD = "yaroslavolga1972"
