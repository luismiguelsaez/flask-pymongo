from flask import Flask, abort
from flask_restful import Resource, Api, request
from flask_pymongo import PyMongo
from os import environ
from json import loads

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/stocks"
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
        data = request.json
        stock_search = mongo.db.stocks.find_one({"id": stock_id})
        if stock_search:
            abort(409, "Stock ID already in database")
        mongo.db.stocks.insert_one({ "id": stock_id, "name": data['name']})
        return {"error":"Stock inserted"}

api.add_resource(Stock, '/<string:stock_id>')

if __name__ == '__main__':
    app.run(debug=True)