import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a_default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost/rigster')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
