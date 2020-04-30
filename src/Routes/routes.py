from pathlib import Path
import os, sys
import argparse

from src.Routes.mongo import update_template_in_mongo, get_all_records_from_collection, update_data_in_mongo

parser = argparse.ArgumentParser(description="Starts the archgraph server.")

parser.add_argument("--neo4j", nargs="?", help="Address of the neo4j server")

parser.add_argument("--mongodb", nargs="?", help="Address of the mongodb server")

args = parser.parse_args()


# returns the project root path (assumes that the script is started from src/Routes/routes.py)
def get_project_root():
    """Returns project root folder."""
    return Path(__file__).parent.parent.parent


# append project root to sys paths so that src.** modules can be found by Python when running the app from a script
# From https://leemendelowitz.github.io/blog/how-does-python-find-packages.html
print("Archgraph running at " + get_project_root().as_posix())
sys.path.append(get_project_root().as_posix())

from flask import Flask, Response, jsonify, make_response, request, send_from_directory

from flask_cors import CORS, cross_origin
from neomodel import config

from src.Utils.JsonEncoder import search_cidoc, search_specific_cidoc
from src.Utils.Utils import get_node_by_uid, delete_node_by_uid, nested_json, updated_node

if args.neo4j:
    config.DATABASE_URL = args.neo4j
else:
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
    node = get_node_by_uid(uid)
    if node is not None:
        return Response(node.encodeJSON(), mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/withtemplate/<uid>", methods=["GET"])
@cross_origin()
def response_get_node_with_templat(uid):
    node = get_node_by_uid(uid)
    template = {
        "E52_Time_Span": {
            "has_value": "DataObject"}
    }
    if node is not None:
        result = nested_json(node, template)
        if result is not None:
            return make_response(jsonify(result), 201)
        else:
            return make_response(jsonify(message="Some error occurred"), 404)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/schema/<uid>", methods=["GET"])
@cross_origin()
def response_get_schema_node(uid):
    node = get_node_by_uid(uid)
    if node is not None:
        return make_response(jsonify(node.getSchema()), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/schemawithtemplate/<uid>", methods=["POST"])
@cross_origin()
def update_schema_of_node_in_mongodb(uid):
    node = get_node_by_uid(uid)
    template = request.json
    if node is not None:
        template_of_node = node.get_schema_with_template(template)
        classes_name = node.get_superclasses_name()
        message = update_template_in_mongo(classes_name, template_of_node)
        get_all_records_from_collection("template")

        return make_response(jsonify(message=message), 200)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/schemawithtemplate/<uid>", methods=["GET"])
@cross_origin()
def response_get_schema_node_with_template(uid):
    node = get_node_by_uid(uid)
    template = {
        "E52_Time_Span": {
            "has_value": "DataObject",
        }
    }
    if node is not None:
        result = node.get_schema_with_template(template)
        return make_response(jsonify(result), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)

# @app.route("/create", methods=["POST"])
# def create():
#     return "create"


# update node
@app.route("/<uid>", methods=["POST"])
@cross_origin()
def response_update(uid):
    template = {
        "E52_Time_Span": {
            "has_value": "DataObject",
        }
    }
    node = get_node_by_uid(uid)
    if node is not None:
        data = request.json
        merged = updated_node(node, data)
        if merged:
            new_data = nested_json(node, template)
            update_data_in_mongo(uid, new_data)
            get_all_records_from_collection("data")
            return make_response(jsonify(new_data), 201)
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
    if result is not None:
        return Response(make_result(result), mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Failed Search"), 404)


@app.route("/search_specific/<entity>/<word>", methods=["GET"])
@cross_origin()
def search_specific(entity, word):
    result = search_specific_cidoc(entity, word)
    if result is not None:
        return Response(make_result(result), mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Failed Search"), 404)


def make_result(result):
    response_array = "[" + result[0].encodeJSON()
    iterator = iter(result)
    next(iterator)
    for items in iterator:
        response_array += ", " + items.encodeJSON()
    response_array += "]"
    return response_array


if __name__ == "__main__":
    app.run()
