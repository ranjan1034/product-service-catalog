from flask_restful import Api

from application import app
from application.routes.auth import RegisterUser
from application.routes.products import ListProducts, AddProduct, GetProductDetails

"""
Flask-RESTful API setup for user registration and product management.

Attributes:
- app (Flask): The Flask application instance.
- api (Api): The Flask-RESTful API instance associated with the Flask app.

Routes:
- '/api/register': Endpoint for user registration.
- '/api/products': Endpoints for managing products (list all, add a new one).
- '/api/products/<string:product_id>': Endpoint for retrieving details of a specific product.

Usage:
- Initialize the Flask app:
  >>> from flask import Flask
  >>> app = Flask(__name__)

- Initialize the Flask-RESTful API:
  >>> from flask_restful import Api
  >>> api = Api(app)

- Register resources (endpoints) with the API:
  >>> from application.routes.auth import RegisterUser
  >>> from application.routes.products import ListProducts, AddProduct, GetProductDetails
  >>> api.add_resource(RegisterUser, '/api/register')
  >>> api.add_resource(ListProducts, '/api/products')
  >>> api.add_resource(AddProduct, '/api/products')
  >>> api.add_resource(GetProductDetails, '/api/products/<string:product_id>')

- Run the application (if executed as the main module):
  >>> if __name__ == '__main__':
  ...    app.run(debug=True)

See Also:
- Flask documentation: https://flask.palletsprojects.com/
- Flask-RESTful documentation: https://flask-restful.readthedocs.io/
"""

api = Api(app)

api.add_resource(RegisterUser, '/api/register')
api.add_resource(ListProducts, '/api/products')
api.add_resource(AddProduct, '/api/products')
api.add_resource(GetProductDetails, '/api/products/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
