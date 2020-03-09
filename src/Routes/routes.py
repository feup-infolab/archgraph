from flask import Flask, Response, jsonify

from neomodel import config
from src.Models.DataObject.v0_0_2.String import String

config.DATABASE_URL = "bolt://neo4j:password@localhost:7687"
app = Flask(__name__, static_url_path="")


@app.route("/<uid>", methods=["GET"])
def view(uid):
    returned_string = String.nodes.get(uid=uid)
    return Response(returned_string.toJSON(), mimetype="application/json")


@app.route("/schema/<uid>", methods=["GET"])
def getSchema(uid):
    returned_string = String.nodes.get(uid=uid)
    return jsonify(returned_string.getSchema())


@app.route("/create")
def create():
    return "create"


@app.route("/<uid>/update")
def update(uid):
    return "update %s" % uid


@app.route("/<uid>/delete")
def delete(uid):
    return "delete %s" % uid


if __name__ == "__main__":
    app.run()
