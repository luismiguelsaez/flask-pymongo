from flask import Flask, abort
from flask_restful import Resource, Api, request, reqparse
from flask_pymongo import PyMongo
from os import environ

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/invest"
mongo = PyMongo(app)
api = Api(app)

class Stock(Resource):

    def get(self, stock_id):
        try:
            stock_search = mongo.db.stocks.find_one({"id": stock_id})
        except:
            abort(500, "Database error")
        if not stock_search:
            abort(404, "Stock ID not found")
        return {"name":stock_search["name"]}, 200

    def put(self, stock_id):

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, help="Stock name is required")
        args = parser.parse_args()

        stock_search = mongo.db.stocks.find_one({"id": stock_id})

        if stock_search:
            abort(409, "Stock ID already in database")

        try:
            mongo.db.stocks.insert_one({ "id": stock_id, "name": args['name'] })
        except:
            abort(500, "Database error")

        return {}, 201

    def delete(self, stock_id):

        try:
            mongo.db.stocks.delete_one({ "id": stock_id })
        except:
            abort(500, "Database error")

        return {}, 200


api.add_resource(Stock, '/<string:stock_id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
