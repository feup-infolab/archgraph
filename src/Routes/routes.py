from flask import Flask, Response, jsonify
import os
from flask import send_from_directory

from neomodel import config
from src.Models.DataObject.v0_0_2.String import String

config.DATABASE_URL = "bolt://neo4j:password@localhost:7687"
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/<uid>", methods=["GET"])
def view(uid):
    returned_string = String.nodes.get(uid=uid)
    Response(returned_string.toJSON(), mimetype="application/json")


@app.route("/schema/<uid>", methods=["GET"])
def getSchema(uid):
    returned_string = String.nodes.get(uid=uid)
    jsonify(returned_string.getSchema())


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
