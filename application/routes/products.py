from flask import request, jsonify
from flask_restful import Resource
from application.models.product import Product

class ListProducts(Resource):
    def get(self):
        products = Product.objects.all()
        return jsonify(products)

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'])
        new_product.save()
        return jsonify(message='Product added successfully')

class GetProductDetails(Resource):
    def get(self, product_id):
        product = Product.objects(id=product_id).first()
        if product:
            return jsonify(product)
        else:
            return jsonify(message='Product not found'), 404
