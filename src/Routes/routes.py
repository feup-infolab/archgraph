import json
from pathlib import Path
import os, sys


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
from src.Utils.Utils import get_node_by_uid, build_next_json, updated_node, make_result, build_information_uidglab, \
    search_identifier_types, search_title_types, dglab_node_update

# import src.Utils.ArgParser as ArgParser

# args = ArgParser.parse()
import src.Utils.EnvVarManager as EnvVarManager

config.DATABASE_URL = (
        "bolt://neo4j:password@"
        + EnvVarManager.get_from_env_or_return_default("NEO4J_HOST", "127.0.0.1")
        + ":"
        + EnvVarManager.get_from_env_or_return_default("NEO4J_PORT", "7687")
)

from src.Routes.mongo import (
    insert_template_in_mongo,
    get_all_records_from_collection,
    get_schema_from_mongo,
    get_templates_from_mongo_by_classes_name,
)

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app = Flask(__name__, static_url_path="")
app.config["JSON_SORT_KEYS"] = False
app.debug = True


@app.before_request
def log_request_info():
    app.logger.debug("Headers: %s", request.headers)
    app.logger.debug("Body: %s", request.get_data())


@app.after_request
def after(response):
    # todo with response
    print(response.status)
    print(response.headers)
    print(response.get_data())
    return response


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


@app.route("/template/<uid>", methods=["GET"])
@cross_origin()
def default_template(uid):
    node = get_node_by_uid(uid)
    if node is not None:
        return make_response(jsonify(node.generate_template()["template"]), 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/withtemplate/<uid>", methods=["POST"])
@cross_origin()
def get_record(uid):
    # template = {
    #     "E52_Time_Span": {
    #         "has_value": "DataObject"}
    # }
    # template = {
    #     "E52_Time_Span": {
    #         "P86_falls_within": "E52_Time_Span"}
    # }
    # record = get_record_from_collection(uid, "data")
    # if record is not None:
    #     return make_response(jsonify(json.loads(record["data"])), 201)
    # else:
    # template = json.loads(template_str)
    template = request.json

    node = get_node_by_uid(uid)
    if node is not None:
        data = build_next_json(node, template)
        # print(data)
        # add_record_to_collection(uid, data, "data")
        get_all_records_from_collection("data")
        if data is not None:
            return make_response(jsonify(data), 201)
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


@app.route("/inserttemplate/<uid>", methods=["POST"])
@cross_origin()
def insert_template_in_mongodb(uid):
    node = get_node_by_uid(uid)

    template = request.json
    # template = {
    #     "E52_Time_Span": {
    #         "P86_falls_within": "E52_Time_Span"}
    # }
    # template = {
    #    "E52_Time_Span": {
    #        "has_value": "DataObject",
    #    }
    # }
    if node is not None:
        schema_of_node = node.get_schema_with_template(template)
        classes_name = node.get_superclasses_name()
        message = insert_template_in_mongo(classes_name, schema_of_node, template)
        print("Received Message")
        print(message)
        get_all_records_from_collection("createdTemplate")
        return make_response(jsonify(message=message), 200)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


# TODO Change below


@app.route("/createwithtemplate/<uid>", methods=["GET"])
@cross_origin()
def response_create_node_with_template(uid):
    node = get_node_by_uid(uid)
    template = {"E52_Time_Span": {}}
    if node is not None:
        result = build_next_json(node, template)
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
    template = {"E52_Time_Span": {}}
    if node is not None:
        result = node.get_schema_with_template(template)
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
    template = {"E52_Time_Span": {}}
    return make_response(jsonify(template), 201)


@app.route("/schemawithtemplate/<uid>", methods=["POST"])
@cross_origin()
def get_schema(uid):
    node = get_node_by_uid(uid)
    # template = {
    #     "E52_Time_Span": {
    #         "has_value": "DataObject"}
    # }

    # template = {
    #     "E52_Time_Span": {
    #         "P86_falls_within": "E52_Time_Span"}
    # }
    template = request.json
    print(template)
    if node is not None:
        result = get_schema_from_mongo(template)
        if result is not None:
            return make_response(jsonify(json.loads(result)), 201)
        else:
            make_response(jsonify(message="Template doesn't exists"), 404)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/templatesfromentity/<uid>", methods=["GET"])
@cross_origin()
def get_templates_from_entity(uid):
    print("lindo")
    node = get_node_by_uid(uid)
    if node is not None:
        get_all_records_from_collection("createdTemplate")
        classes_name = node.get_superclasses_name()
        templates = get_templates_from_mongo_by_classes_name(classes_name)
        if templates is None:
            return make_response(
                jsonify(message="Don't have templates for this entity"), 200
            )
        else:
            test = jsonify(templates)
            return make_response(test, 201)
    else:
        return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/uidglab/<uid>", methods=["GET"])
@cross_origin()
def response_uidglab_view(uid):
    node = get_node_by_uid(uid)
    if node.__class__.__name__ is not "E24_Physical_Human_Made_ThingSchema" or node.__class__.__name__ is not "E18_Physical_ThingSchema":
        if node is not None:
            response = build_information_uidglab(node)
            if response:
                return make_response(jsonify(response), 201)
            else:
                make_response(jsonify(message="Node doesn't have information"), 404)
        else:
            return make_response(jsonify(message="Node doesn't exists"), 404)
    else:
        return make_response(jsonify(message="Node is not a valid type"), 404)


@app.route("/uidglab/<uid>", methods=["POST"])
@cross_origin()
def response_uidglab_edit(uid):
    node = get_node_by_uid(uid)
    if node.__class__.__name__ is not "E24_Physical_Human_Made_ThingSchema" or node.__class__.__name__ is not "E18_Physical_ThingSchema":
        if node is not None:
            data = request.json
            identifiers = data.get("identifier", None)
            titles = data.get("title", None)
            if dglab_node_update(node, identifiers, titles):
                response = build_information_uidglab(node)
                if response:
                    return make_response(jsonify(response), 201)
                else:
                    return make_response(jsonify(message="Node doesn't have information"), 404)
            else:
                return make_response(jsonify(message="Unsaved node"), 404)
        else:
            return make_response(jsonify(message="Node doesn't exists"), 404)
    else:
        return make_response(jsonify(message="Node is not a valid type"), 404)


@app.route("/control_values/identifier_types", methods=["GET"])
@cross_origin()
def response_type_identifiers():
    response = search_identifier_types()
    if response:
        return make_response(jsonify(response), 201)
    else:
        return make_response(jsonify(message="Doesn't have information"), 404)


@app.route("/control_values/title_types", methods=["GET"])
@cross_origin()
def response_type_titles():
    response = search_title_types()
    if response:
        return make_response(jsonify(response), 201)
    else:
        return make_response(jsonify(message="Doesn't have information"), 404)


# update node
@app.route("/<uid>", methods=["POST"])
@cross_origin()
def response_update(uid):
    node = get_node_by_uid(uid)
    if node is not None:
        data = request.json
        merged = updated_node(node, data["data"], data["template"])
        if merged:
            # update_data_in_mongo(uid, node.encodeJSON())
            # get_all_records_from_collection("data")
            new_data = build_next_json(node, data["template"])
            return make_response(jsonify(new_data), 201)
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


# @app.route("/<uid>", methods=["DELETE"])
# @cross_origin()
# def delete(uid):
#     result = delete_node_by_uid(uid)
#     if result is not None:
#         return make_response(jsonify(message="Successfully deleted node"), 201)
#     else:
#         return make_response(jsonify(message="Node doesn't exists"), 404)


@app.route("/search", defaults={"query": None}, methods=["GET"])
@app.route("/search/<query>", methods=["GET"])
@cross_origin()
def search(query):
    result = search_cidoc(query)
    if result is not None:
        return Response(make_result(result), mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Failed Search"), 404)


@app.route("/search_specific/<class_name>", defaults={"query": None}, methods=["GET"])
@app.route("/search_specific/<class_name>/<query>", methods=["GET"])
@cross_origin()
def search_specific(class_name, query):
    result = search_specific_cidoc(class_name, query)
    if result is not None:
        return Response(make_result(result), mimetype="application/json", status=201)
    else:
        return make_response(jsonify(message="Failed Search"), 404)


# delete_collection("defaultTemplate")
# json = read_file("../Utils/defaultTemplates.json")
# populate_template_collection(json)
# get_all_records_from_collection("createdTemplate")
if __name__ == "__main__":
    host = EnvVarManager.get_from_env_or_return_default(
        "CUSTOM_HOST_FOR_SERVER_BIND", "127.0.0.1"
    )
    if host is not None and host != "127.0.0.1":
        app.logger.debug("Archgraph running with a custom host setting: %s", host)
    app.run(host=host)
