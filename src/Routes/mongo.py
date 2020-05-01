import json
from datetime import datetime
from src.Utils.Utils import find_name_of_class_schema_in_project


from pymongo import MongoClient

client = MongoClient(port=27017, username="root", password="rootpassword")
db = client.mydatabase
date_now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")


# def insert_into_mongo(content):
#     result = {}
#     if isinstance(content, type([])):
#         db.reviews.insert_many(content)
#         print("inserted many documents")
#
#     elif isinstance(content, type({})):
#         result = db.reviews.insert_one(content)
#         print(result.inserted_id)
#
#     cursor = db.reviews.find({})
#     for document in cursor:
#         print(document)
def populate_template_collection(objectjson):

    for object in objectjson:
        class_name = object["className"]

        class_in_project = find_name_of_class_schema_in_project(class_name)
        if class_in_project is None:
            print(class_name + " did't found")
        template = object["template"]
        schema = class_in_project().getSchema()
        schema_str = json.dumps(schema)
        db.defaultTemplate.insert_one({"class_name": class_name, "template": template, "schema": schema_str})
    return


def update_data_in_mongo(uid, data):
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d, %H:%M:%S")
    result = db.data.find_one({"uid": uid})
    if result is None:
        db.data.insert_one({"uid": uid, "data": data, "timestamp": date_str})
        print("created")
    else:
        db.data.find_one_and_replace({"_id": result["_id"]}, {"uid": uid, "data": data, "timestamp": date_str})
        print("updated")


def update_schema_in_mongo(classes_name, schema):
    schema_str = json.dumps(schema)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d, %H:%M:%S")
    message = ""
    result = get_schema_from_mongo(classes_name)
    if result is None:
        message = "was inserted new template"
        db.template.insert_one({'classes_name': classes_name, "timestamp": date_str, "schema": schema_str})
        return message
    elif result['match'] < len(classes_name):
        db.template.insert_one({'classes_name': classes_name, "timestamp": date_str, "schema": schema_str})
        message = "inserted new template"
    else:
        db.data.find_one_and_replace({"_id": result['_id']}, {'classes_name': classes_name, "timestamp": date_str, "schema": schema})
        message = "updated template"
    return message


def get_schema_from_mongo(classes_name):
    if db.template.count_documents({'classes_name': {'$in': classes_name}}) == 0:
        return None
    else:
        result = db.template.find({'classes_name': {'$in': classes_name}})

        elements_match_records = {
            '_id': "",
            'match': 0,
            'schema': {}
        }
        for document in result:
            merged = set(classes_name) & set(document['classes_name'])
            if len(merged) > elements_match_records["match"]:
                elements_match_records['match'] = len(merged)
                elements_match_records['schema'] = document
                elements_match_records['_id'] = document['_id']
        return elements_match_records


def get_record_from_collection(uid, collection):
    record = db[collection].find_one({"uid": uid})
    return record


def add_record_to_collection(uid, data, collection):
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d, %H:%M:%S")
    db[collection].insert_one({"uid": uid, "data": data, "timestamp": date_str})
    return


def get_all_records_from_collection(collection):
    records = db[collection].find({})
    for record in records:
        print(record)
    return records


def delete_collection(collection):
    db[collection].delete_many({})


delete_collection("data")
delete_collection("template")

# unique = datetime.now()
# #update_data(5552,"aaa")
# class_name = ['ola', '1', '2', '3']
# db.template.insert_one({'classes_name': class_name, "timestamp": date_now, "template": "template"})
#
# class_name2 = ['ola', '3', "4"]
# db.template.insert_one({'classes_name': class_name2, "timestamp": date_now, "template": "template"})
#
# class_name_test = ["7"]
# update_template(class_name_test, "template")
#
#
# print("get all records")
# get_all_records_from_collection("template")
#get_all_records_from_collection("data")
