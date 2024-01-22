from flask_restful import Api

from application import app
from application.routes.auth import RegisterUser
from application.routes.products import ListProducts, AddProduct, GetProductDetails

api = Api(app)

api.add_resource(RegisterUser, '/api/register')
api.add_resource(ListProducts, '/api/products')
api.add_resource(AddProduct, '/api/products')
api.add_resource(GetProductDetails, '/api/products/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
