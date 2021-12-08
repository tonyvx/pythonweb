from flask import Flask
from flask_pymongo import PyMongo
import json
from bson.json_util import dumps

from pyMongoConnection import reviews


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongouser:mongopassword@localhost:27017/business?authSource=admin"
mongo = PyMongo(app)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/reviews')
def reviewsRoute():
    resp = []
    for row in mongo.db.reviews.find({}):
        resp.append(row)
        print(row)
    # print(json.dumps(resp))
    return dumps(resp)
    # return reviews()
