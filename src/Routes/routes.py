from pathlib import Path
import os, sys
import argparse

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
            "has_value": "DataObject",
            "P1_is_identified_by": "E41_Appellation"}
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


# TODO Change below


@app.route("/createwithtemplate/<uid>", methods=["GET"])
@cross_origin()
def response_create_node_with_template(uid):
    node = get_node_by_uid(uid)
    print(node.get_all_properties_from_entity())
    template = {
        "E52_Time_Span": {}
    }
    if node is not None:
        result = nested_json(node, template)
        if result is not None:
            print("ONE")
            print(result)
            return make_response(jsonify(result), 201)
        else:
            return make_response(jsonify(message="Some error occurred"), 404)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/createtemplate/<uid>", methods=["GET"])
@cross_origin()
def create_base_schema_node_with_template(uid):
    node = get_node_by_uid(uid)
    template = {
        "E52_Time_Span": {}
    }
    if node is not None:
        result = node.get_schema_with_template(template)
        print("TWO")
        print(result)
        return make_response(jsonify(result), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/getallproperties/<uid>", methods=["GET"])
@cross_origin()
def get_all_node_properties(uid):
    node = get_node_by_uid(uid)
    property_array = node.get_all_properties_from_entity()
    if node is not None:
        return make_response(jsonify(property_array), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/obtainschema", methods=["GET"])
@cross_origin()
def get_template():
    template = {
        "E52_Time_Span": {}
    }
    return make_response(jsonify(template), 201)


# @app.route("/create", methods=["POST"])
# def create():
#     return "create"

# TODO Change Above

# update node
@app.route("/<uid>", methods=["POST"])
@cross_origin()
def response_update(uid):
    node = get_node_by_uid(uid)
    if node is not None:
        data = request.json
        print(data)
        merged = updated_node(node, data)
        if merged:
            return make_response(jsonify(node.encodeJSON()), 201)
        else:
            return make_response(jsonify(message="Unsaved node"), 404)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/post_template", methods=["POST"])
@cross_origin()
def receive_new_template():
    data = request.json
    print("Returned Schema")
    print(data)
    return make_response(jsonify(data), 201)


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
