import os


class Config:
    """Main configurations class"""

    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://orukopius:blog@localhost/tenant'
    SECRET_KEY = '@jkloruko'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'OkoaTenant'
    SENDER_EMAIL = 'orukopius8@gmail.com'


class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://orukopius:blog@localhost/tenant'


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}