from flask import Flask, abort
from flask_restful import Resource, Api, request, reqparse
from flask_pymongo import PyMongo
from os import environ
import logging


MONGO_HOST = environ["MONGO_HOST"] if "MONGO_HOST" in environ else "localhost"
MONGO_PORT = environ["MONGO_PORT"] if "MONGO_PORT" in environ else "27017"
MONGO_DB = environ["MONGO_DB"] if "MONGO_DB" in environ else "test"

app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s : %(message)s"
)

app.config["MONGO_URI"] = "mongodb://" + MONGO_HOST + ":" + MONGO_PORT + "/" + MONGO_DB
mongo = PyMongo(app)
api = Api(app)

class Stock(Resource):

    def get(self, stock_id):

        try:
            stock_search = mongo.db.stocks.find_one({"id": stock_id},{"_id": False})
        except:
            app.logger.critical("Database connection error")
            abort(500, "Database error")

        if not stock_search:
            app.logger.info("Stock ID [" + stock_id + "] not found in database")
            abort(404, "Stock ID not found")

        return stock_search, 200

    def put(self, stock_id):

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, help="Stock name is required")
        args = parser.parse_args()

        stock_search = mongo.db.stocks.find_one({"id": stock_id})

        if stock_search:
            app.logger.info("Stock ID [" + stock_id + "] already in database")
            abort(409, "Stock ID already in database")

        try:
            mongo.db.stocks.insert_one({ "id": stock_id, "name": args['name'] })
        except:
            app.logger.critical("Database connection error")
            abort(500, "Database error")

        return {}, 201

    def post(self, stock_id):

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, help="Stock name is required")
        args = parser.parse_args()

        try:
            mongo.db.stocks.update_one({"id": stock_id},{ "$set": { "name": args['name'] } })
        except:
            app.logger.critical("Database connection error")
            abort(500, "Database error")

        return {}, 204

    def delete(self, stock_id):

        try:
            mongo.db.stocks.delete_one({ "id": stock_id })
        except:
            app.logger.critical("Database connection error")
            abort(500, "Database error")

        return {}, 200


api.add_resource(Stock, '/<string:stock_id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
