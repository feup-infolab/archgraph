import json
from datetime import datetime
from src.Utils.Utils import find_name_of_class_schema_in_project

from pymongo import MongoClient

client = MongoClient(port=27017, username="root", password="rootpassword")
db = client.mydatabase
date_now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")


def insert_default_templates(templates):
    for template in templates:
        class_name = template["class_name"]
        schema = template["schema"]
        db.defaultTemplate.insert_one({"class_name": class_name, "template": template["template"], "schema": schema})
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


def insert_template_in_mongo(classes_name, schema, template):
    schema_str = json.dumps(schema)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d, %H:%M:%S")
    result = get_schema_from_mongo(template)
    if result is None:
        db.createdTemplate.insert_one(
            {'classes_name': classes_name, "timestamp": date_str, "schema": schema_str, "template": template})
        message = "was inserted new template"
        return message
    else:
        message = "template already exists"
        return message


def get_schema_from_mongo(template):
    records = db.createdTemplate.find({'template': template})
    if records.count() == 0:
        return None
    else:
        return records[0]


def get_templates_from_mongo_by_classes_name(classes_name):
    records = db.createdTemplate.find({'classes_name': {'$in': classes_name}})
    default_template = get_default_templates_from_mongo(classes_name)
    result = []

    if records.count() == 0 and default_template is None:
        return None
    else:
        if default_template is not None:
            for template in default_template:
                result.append(template)
        for record in records:
            result.append(record["template"])
        return result


def get_default_templates_from_mongo(classes_name):
    if db.defaultTemplate.count_documents({'classes_name': {'$in': classes_name}}) == 0:
        return None
    else:
        result = db.defaultTemplate.find({'classes_name': {'$in': classes_name}})
        templates = []

        for document in result:
            templates.append(document["template"])
        return templates


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



# unique = datetime.now()
# #update_data(5552,"aaa")
# class_name = ['ola', '1', '2', '3']
# db.createdTemplate.insert_one({'classes_name': class_name, "timestamp": date_now, "template": "template"})
#
# class_name2 = ['ola', '3', "4"]
# db.createdTemplate.insert_one({'classes_name': class_name2, "timestamp": date_now, "template": "template"})
#
# class_name_test = ["7"]
# update_template(class_name_test, "template")
#
#
# print("get all records")
# get_all_records_from_collection("createdTemplate")
# delete_collection("createdTemplate")
# delete_collection("defaultTemplate")
# get_all_records_from_collection("data")
