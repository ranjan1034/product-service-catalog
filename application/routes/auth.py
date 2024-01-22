from flask import request, jsonify
from flask_restful import Resource
from application import db
from application.models.user import User

class RegisterUser(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message='User registered successfully')