from flask_mongoengine import MongoEngine

db_mongo = MongoEngine()


class Product(db_mongo.Document):
    """
        MongoDB Document model representing a product.

        Attributes:
        - name (str): The name of the product. Required and must be unique.
        - price (float): The price of the product. Required.

        Usage:
        - To create a new product instance:
          >>> new_product = Product(name="Example Product", price=19.99)
          >>> new_product.save()

        - To query products:
          >>> all_products = Product.objects.all()
          >>> expensive_products = Product.objects(price__gt=50.0)

        Note:
        - This class is based on the Flask-MongoEngine extension and inherits from `db_mongo.Document`.

        See Also:
        - Flask-MongoEngine documentation: https://flask-mongoengine.readthedocs.io/
        """
    name = db_mongo.StringField(required=True, unique=True)
    price = db_mongo.FloatField(required=True)
