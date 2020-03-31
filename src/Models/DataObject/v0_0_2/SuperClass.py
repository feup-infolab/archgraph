import datetime
import json

from marshmallow_jsonschema import JSONSchema


class SuperClass:
    def __init__(self, schema):
        self.schema = schema

    def getSchema(self):
        json_schema = JSONSchema()
        return json_schema.dump(self.schema)

    # Json to string
    def encodeJSON(self):
        data = {}
        for key, val in self.__dict__.items():
            if (key != "schema") and (key != "id"):
                data[key] = val

        def my_converter(o):
            if isinstance(o, datetime.datetime):
                return o.strftime("%Y-%m-%d")

        return json.dumps(data, default=my_converter)

    # string to json
    def decodeJSON(self):
        return json.loads(self.encodeJSON())
