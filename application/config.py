import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_here'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    MONGO_URI = 'mongodb://mongo:27017/products'

class ProductionConfig(Config):
    # Define production configurations here
    pass