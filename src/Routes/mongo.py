import json

from pymongo import MongoClient

client = MongoClient(port=27017, username="root", password="rootpassword")
db = client.mydatabase


def read_file(path_file):
    file = open(path_file, "r")
    file_to_json = json.loads(file.read())
    print(file_to_json)
    return file_to_json


def insert_into_mongo(content):
    result = {}
    if isinstance(content, type([])):
        db.reviews.insert_many(content)
        print("inserted many documents")

    elif isinstance(content, type({})):
        result = db.reviews.insert_one(content)
        print(result.inserted_id)

    cursor = db.reviews.find({})
    for document in cursor:
        print(document)


def delete_databse():
    db.reviews.delete_many({})
