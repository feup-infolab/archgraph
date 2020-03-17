import json

from marshmallow_jsonschema import JSONSchema


class SerializeClass:
    def __init__(self, schema):
        self.schema = schema

    def getSchema(self):
        json_schema = JSONSchema()
        return json_schema.dump(self.schema)

    def toJSON(self):
        r = "{"
        r = r + ', '.join(
            '"{}": "{}"'.format(key, val) for key, val in self.__dict__.items() if key is not "schema")
        r = r + "}"
        return json.dumps(eval(r))
