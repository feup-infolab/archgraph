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
        r = "{"
        r = r + ", ".join(
            '"{}": "{}"'.format(key, val)
            for key, val in self.__dict__.items()
            if key is not "schema"
            if key is not "id"
        )
        r = r + "}"
        return json.dumps(eval(r))

    # string to json
    def decodeJSON(self):
        return json.loads(self.encodeJSON())
