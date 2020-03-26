import os

from flask import (Flask, Response, jsonify, make_response, request,
                   send_from_directory)

from flask_cors import CORS, cross_origin
from neomodel import config
# TODO nao apagar estes importes
from src.Models.DataObject.v0_0_2.DataObject import DataObject
from src.Models.DataObject.v0_0_2.Approximate import Approximate
from src.Models.DataObject.v0_0_2.AuthorityFile import AuthorityFile
from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString
from src.Models.DataObject.v0_0_2.Boolean import Boolean
from src.Models.DataObject.v0_0_2.Date import Date
from src.Models.DataObject.v0_0_2.Decimal import Decimal
from src.Models.DataObject.v0_0_2.GeospatialCoordinates import \
    GeospatialCoordinates
from src.Models.DataObject.v0_0_2.Instant import Instant
from src.Models.DataObject.v0_0_2.Integer import Integer
from src.Models.DataObject.v0_0_2.Interval import Interval
from src.Models.DataObject.v0_0_2.Latitude import Latitude
from src.Models.DataObject.v0_0_2.Longitude import Longitude
from src.Models.DataObject.v0_0_2.PersonName import PersonName
from src.Models.DataObject.v0_0_2.Polygon import Polygon
from src.Models.DataObject.v0_0_2.RegexString import RegexString
from src.Models.DataObject.v0_0_2.String import String
# TODO nao apagar estes importes

config.DATABASE_URL = "bolt://neo4j:password@localhost:7687"

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


app = Flask(__name__, static_url_path="")


def getNodeByUid(uid):
    try:
        return DataObject.nodes.get(uid=uid)
    except BaseException as e:
        print(e)
        return None


def deleteNodeByUid(uid):
    try:
        node = DataObject.nodes.get(uid=uid)
        node.delete()
        return True
    except BaseException:
        return None


@app.route("/<uid>", methods=["GET"])
@cross_origin()
def responseGetNode(uid):
    result = getNodeByUid(uid)
    if result is not None:
        return Response(result.encodeJSON(), mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/schema/<uid>", methods=["GET"])
@cross_origin()
def responseGetSchemaNode(uid):
    result = getNodeByUid(uid)
    if result is not None:
        return make_response(jsonify(result.getSchema()), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/create", methods=["POST"])
def create():
    return "create"  # TODO


# update node
@app.route("/<uid>", methods=["POST"])
@cross_origin()
def responseUpdate(uid):
    node = getNodeByUid(uid)
    if node is not None:
        data = request.json
        merged = node.merge_node(data)
        if merged:
            return Response(node.encodeJSON(), mimetype="application/json", status=201)
        else:
            return make_response(jsonify(message="Unsaved node"), 404)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/<uid>", methods=["DELETE"])
@cross_origin()
def delete(uid):
    result = deleteNodeByUid(uid)
    if result is not None:
        return make_response(jsonify(message="Successfully deleted node"), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


if __name__ == "__main__":
    app.run()

# from pymongo import MongoClient
# from random import randint
#
# client = MongoClient(port=27017, username="root", password="rootpassword")
# db = client.mydatabase
#
# names = ['Kitchen', 'Animal', 'State']
# company_type = ['LLC', 'Inc', 'Company']
# company_cuisine = ['Pizza', 'Bar Food']
# for x in range(1, 2):
#     business = {
#         'name': names[randint(0, (len(names) - 1))] + ' ' + names[randint(0, (len(names) - 1))] + ' ' + company_type[
#             randint(0, (len(company_type) - 1))],
#         'rating': randint(1, 5),
#         'cuisine': company_cuisine[randint(0, (len(company_cuisine) - 1))]
#     }
#     # Step 3: Insert business object directly into MongoDB via isnert_one
#     result = db.reviews.insert_one(business)
#     print(db.reviews.find_one())
#     # Step 4: Print to the console the ObjectID of the new document
#     print('Created {0} of 10 as {1}'.format(x, result.inserted_id))
# # Step 5: Tell us that you are done
# print('finished creating 10 business reviews')
