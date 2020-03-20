import os

import flask
from flask import request, make_response
from flask import Flask, Response, jsonify, send_from_directory

from flask_cors import CORS, cross_origin
from neomodel import config
from src.Models.DataObject.v0_0_2.Approximate import Approximate
from src.Models.DataObject.v0_0_2.AuthorityFile import AuthorityFile
from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString
from src.Models.DataObject.v0_0_2.Boolean import Boolean
from src.Models.DataObject.v0_0_2.DataObject import DataObject
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
    except:
        return None


def deleteNodeByUid(uid):
    try:
        node = DataObject.nodes.get(uid=uid)
        node.delete()
        return True
    except:
        return None


# def getNode(node_type, uid):
#     switcher = {
#         "approximate": getNodeByUid(Approximate, uid),
#         "authorityfile": getNodeByUid(AuthorityFile, uid),
#         "authoritystring": getNodeByUid(AuthorityString, uid),
#         "boolean": getNodeByUid(Boolean, uid),
#         "dataobject": getNodeByUid(DataObject, uid),
#         "date": getNodeByUid(Date, uid),
#         "decimal": getNodeByUid(Decimal, uid),
#         "geospatialcoordinates": getNodeByUid(GeospatialCoordinates, uid),
#         "instant": getNodeByUid(Instant, uid),
#         "integer": getNodeByUid(Integer, uid),
#         "interval": getNodeByUid(Interval, uid),
#         "latitude": getNodeByUid(Latitude, uid),
#         "longitude": getNodeByUid(Longitude, uid),
#         "personname": getNodeByUid(PersonName, uid),
#         "polygon": getNodeByUid(Polygon, uid),
#         "regexstring": getNodeByUid(RegexString, uid),
#         "string": getNodeByUid(String, uid),
#     }
#     return switcher.get(node_type.lower(), "None")


@app.route("/<uid>", methods=["GET"])
@cross_origin()
def responseGetNode(uid):
    result = getNodeByUid(uid)
    if result is not None:
        return Response(result.toJSON(), mimetype="application/json", status=200)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/schema/<uid>", methods=["GET"])
@cross_origin()
def responseGetSchemaNode(uid):
    result = getNodeByUid(uid)
    if result is not None:
        return jsonify(result.getSchema())
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/create", methods=["POST"])
def create():
    return "create"


# update node
@app.route("/<uid>", methods=["POST"])
@cross_origin()
def responseUpdate(uid):
    node = getNodeByUid(uid)
    if node is not None:
        data = request.json
        return jsonify(data)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/<uid>", methods=["DELETE"])
@cross_origin()
def delete(uid):
    result = deleteNodeByUid(uid)
    if result is not None:
        return jsonify()
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


if __name__ == "__main__":
    app.run()
