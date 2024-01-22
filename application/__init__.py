from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
Flask application setup with SQLAlchemy integration.

Attributes:
- app (Flask): The Flask application instance.
- db (SQLAlchemy): The SQLAlchemy database instance associated with the Flask app.

Usage:
- Initialize the Flask app:
  >>> from flask import Flask
  >>> app = Flask(__name__)

- Load configuration (in this case, DevelopmentConfig):
  >>> app.config.from_object('application.config.DevelopmentConfig')

- Initialize the SQLAlchemy database:
  >>> from flask_sqlalchemy import SQLAlchemy
  >>> db = SQLAlchemy(app)

Note:
- Ensure that you have configured your Flask app properly, including setting up the necessary configurations in 'application.config.DevelopmentConfig'.
- The SQLAlchemy database instance is associated with the Flask app using 'SQLAlchemy(app)'.

See Also:
- Flask documentation: https://flask.palletsprojects.com/
- Flask-SQLAlchemy documentation: https://flask-sqlalchemy.palletsprojects.com/
"""

app = Flask(__name__)
app.config.from_object('application.config.DevelopmentConfig')

db = SQLAlchemy(app)