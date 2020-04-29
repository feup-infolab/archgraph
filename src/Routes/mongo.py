import json
from datetime import datetime


from pymongo import MongoClient

client = MongoClient(port=27017, username="root", password="rootpassword")
db = client.mydatabase
date_now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

# def read_file(path_file):
#     file = open(path_file, "r")
#     file_to_json = json.loads(file.read())
#     print(file_to_json)
#     return file_to_json
#
#
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


def update_data(uid, data):
    result = db.data.find_one({"uid": uid})
    if result is None:
        db.data.insert_one({"uid": uid, "data": data})
        print("created")
    else:
        new_node = db.data.find_one_and_replace({"_id": result["_id"]}, {"data": data})
        print("updated")
        print(new_node)


def update_template(classes_name, template):
    template_str = json.dumps(template)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d, %H:%M:%S")
    message = ""
    if db.template.count_documents({'classes_name': {'$in': classes_name}}) == 0:
        message = "was inserted new template"
        print(message)
        db.template.insert_one({'classes_name': classes_name, "timestamp": date_str, "template": template_str})
        return message
    else:
        result = db.template.find({'classes_name': {'$in': classes_name}})

        elements_match_records = {
            '_id': "",
            'match': 0,
            'template': {}
        }
        for document in result:
            merged = set(classes_name) & set(document['classes_name'])
            if len(merged) > elements_match_records["match"]:
                elements_match_records['match'] = len(merged)
                elements_match_records['template'] = document
                elements_match_records['_id'] = document['_id']

        if elements_match_records['match'] < len(classes_name):
            db.template.insert_one({'classes_name': classes_name, "timestamp": date_str, "template": template_str})
            elements_match_records['match'] = len(classes_name)
            elements_match_records['template'] = template
            message = "inserted new template"
            print(message)
        else:
            db.data.find_one_and_replace({"_id": elements_match_records['_id']}, {'classes_name': classes_name, "timestamp": date_str, "template": template})
            message = "updated template"
            print(message)
        return message


def get_all_records_from_collection(collection):
    records = db[collection].find({})
    for record in records:
        print(record)
    return records


def delete_collection(collection):
    db[collection].delete_many({})


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
