from pathlib import Path
import os, sys

# returns the project root path (assumes that the script is started from src/Routes/routes.py)
def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent.parent

# append project root to sys paths so that src.** modules can be found by Python when running the app from a script
# From https://leemendelowitz.github.io/blog/how-does-python-find-packages.html
print("Archgraph running at " + get_project_root().as_posix())
sys.path.append(get_project_root().as_posix())

from flask import (Flask, Response, jsonify, make_response, request,
                   send_from_directory)

from flask_cors import CORS, cross_origin
from neomodel import config

from src.Utils.JsonEncoder import search_cidoc, search_specific_cidoc
from src.Utils.Utils import get_node_by_uid, delete_node_by_uid

config.DATABASE_URL = "bolt://neo4j:password@localhost:7687"

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app = Flask(__name__, static_url_path="")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/<uid>", methods=["GET"])
@cross_origin()
def response_get_node(uid):
    result = get_node_by_uid(uid)
    if result is not None:
        return Response(result.encodeJSON(), mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/schema/<uid>", methods=["GET"])
@cross_origin()
def response_get_schema_node(uid):
    result = get_node_by_uid(uid)
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
def response_update(uid):
    node = get_node_by_uid(uid)
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
    result = delete_node_by_uid(uid)
    if result is not None:
        return make_response(jsonify(message="Successfully deleted node"), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/search/<word>", methods=["GET"])
@cross_origin()
def search(word):
    result = search_cidoc(word)
    response_array = "["
    response_array += result[0].encodeJSON()
    iterresult = iter(result)
    next(iterresult)
    for items in iterresult:
        response_array += ", "
        response_array += items.encodeJSON()
    response_array += "]"
    if result is not None:
        return Response(response_array, mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Failed Search"), 404)


@app.route("/search_specific/<entity>/<word>", methods=["GET"])
@cross_origin()
def search_specific(entity, word):
    result = search_specific_cidoc(entity, word)
    response_array = "["
    response_array += result[0].encodeJSON()
    iterresult = iter(result)
    next(iterresult)
    for items in iterresult:
        response_array += ", "
        response_array += items.encodeJSON()
    response_array += "]"
    if result is not None:
        return Response(response_array, mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Failed Search"), 404)


if __name__ == "__main__":
    app.run()
