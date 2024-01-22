"""
Configuration classes for Flask application settings.

Classes:
- Config: Base configuration class with common settings.
- DevelopmentConfig: Configuration class for development environment.
- ProductionConfig: Configuration class for production environment.

Attributes (Common to all Configurations):
- SQLALCHEMY_TRACK_MODIFICATIONS (bool): Track modifications to database objects. Set to False.
- SECRET_KEY (str): Secret key for protecting against Cross-Site Request Forgery (CSRF) attacks.

Attributes (Additional for DevelopmentConfig):
- SQLALCHEMY_DATABASE_URI (str): Database URI for the SQLite database in development.
- MONGO_URI (str): MongoDB URI for connecting to the 'products' database.

Attributes (Additional for ProductionConfig):
- (Define production-specific configurations here if needed)

Usage:
- Choose the appropriate configuration class based on the deployment environment.
  >>> from application.config import DevelopmentConfig, ProductionConfig
  >>> app.config.from_object(DevelopmentConfig)  # or ProductionConfig

Note:
- The 'SQLALCHEMY_TRACK_MODIFICATIONS' setting is set to False to avoid excessive overhead.
- 'SECRET_KEY' is used for securing session cookies and other security-related features.
- Make sure to keep the 'SECRET_KEY' secret and secure.

See Also:
- Flask Configuration documentation: https://flask.palletsprojects.com/en/2.1.x/config/
- Flask-SQLAlchemy documentation: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
- Flask-MongoEngine documentation: https://flask-mongoengine.readthedocs.io/en/latest/
"""
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_here'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    MONGO_URI = 'mongodb://mongo:27017/products'

class ProductionConfig(Config):
    # Define production configurations here
    pass