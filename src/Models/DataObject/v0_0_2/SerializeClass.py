import json

from marshmallow_jsonschema import JSONSchema


class SerializeClass:
    def __init__(self, schema):
        self.list = []
        self.schema = schema

    def getSchema(self):
        json_schema = JSONSchema()
        return json_schema.dump(self.schema)

    def toJSON(self):
        return json.dumps(self.list, default=lambda o: o.__dict__)
