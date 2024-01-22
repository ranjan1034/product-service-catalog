from flask_mongoengine import MongoEngine

db_mongo = MongoEngine()


class Product(db_mongo.Document):
    name = db_mongo.StringField(required=True, unique=True)
    price = db_mongo.FloatField(required=True)
