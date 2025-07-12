import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    FLASK_DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    FLASK_DEBUG = False

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    FLASK_DEBUG = True
    TESTING = True