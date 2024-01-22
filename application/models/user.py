from application import db

class User(db.Model):
    """
        SQLAlchemy Model representing a user in the application.

        Attributes:
        - id (int): Primary key identifier for the user.
        - username (str): Unique username for the user. Cannot be null.
        - password (str): Password for the user. Cannot be null.

        Usage:
        - To create a new user instance:
          >>> new_user = User(username="example_user", password="secure_password")
          >>> db.session.add(new_user)
          >>> db.session.commit()

        - To query users:
          >>> all_users = User.query.all()
          >>> specific_user = User.query.filter_by(username="example_user").first()

        Note:
        - This class is based on the SQLAlchemy ORM and inherits from `db.Model`.
        - Ensure that you have initialized the `db` instance properly before using this class.

        See Also:
        - SQLAlchemy documentation: https://docs.sqlalchemy.org/en/
        """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)