from flask import Flask, Response, jsonify
import os
from flask import send_from_directory
from neomodel import config
from src.Models.DataObject.v0_0_2.Approximate import Approximate
from src.Models.DataObject.v0_0_2.AuthorityFile import AuthorityFile
from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString
from src.Models.DataObject.v0_0_2.Boolean import Boolean
from src.Models.DataObject.v0_0_2.DataObject import DataObject
from src.Models.DataObject.v0_0_2.Date import Date
from src.Models.DataObject.v0_0_2.Decimal import Decimal
from src.Models.DataObject.v0_0_2.GeospatialCoordinates import GeospatialCoordinates
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


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


app = Flask(__name__, static_url_path="")


def getNodeByUid(__class, uid):
    try:
        return __class.nodes.get(uid=uid)
    except:
        return None


def getNode(node_type, uid):
    switcher = {
        "approximate": getNodeByUid(Approximate, uid),
        "authorityfile": getNodeByUid(AuthorityFile, uid),
        "authoritystring": getNodeByUid(AuthorityString, uid),
        "boolean": getNodeByUid(Boolean, uid),
        "dataobject": getNodeByUid(DataObject, uid),
        "date": getNodeByUid(Date, uid),
        "decimal": getNodeByUid(Decimal, uid),
        "geospatialcoordinates": getNodeByUid(GeospatialCoordinates, uid),
        "instant": getNodeByUid(Instant, uid),
        "integer": getNodeByUid(Integer, uid),
        "interval": getNodeByUid(Interval, uid),
        "latitude": getNodeByUid(Latitude, uid),
        "longitude": getNodeByUid(Longitude, uid),
        "personname": getNodeByUid(PersonName, uid),
        "polygon": getNodeByUid(Polygon, uid),
        "regexstring": getNodeByUid(RegexString, uid),
        "string": getNodeByUid(String, uid)
    }
    return switcher.get(node_type.lower(), "None")


@app.route("/<node_type>/<uid>", methods=["GET"])
def responseGetNode(node_type, uid):
    result = getNode(node_type, uid)
    if result is not None:
        return Response(result.toJSON(), mimetype="application/json", status=200)
    else:
        return Response("Node Does Not exists", status=400)


@app.route("/schema/<node_type>/<uid>", methods=["GET"])
def responseGetSchemaNode(node_type, uid):
    result = getNode(node_type, uid)
    if result is not None:
        return jsonify(result.getSchema())
    else:
        return Response("Node Does Not exists", status=400)


@app.route("/create", methods=["POST"])
def create():
    return "create"


# update node
@app.route("/<node_type>/<uid>", methods=["POST"])
def update(node_type, uid):
    return "update %s" % uid


@app.route("/<node_type>/<uid>", methods=["DELETE"])
def delete(node_type, uid):
    return "delete %s" % uid


if __name__ == "__main__":
    app.run()
