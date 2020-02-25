import json
from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import RegexProperty
from src.Models.DataObject.v0_0_2.String import String


class RegexString(String):
    hasRegex = RegexProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def getSchema(self):
        regex_string_schema = RegexStringSchema()
        json_schema = JSONSchema()
        return json_schema.dump(regex_string_schema)


class RegexStringSchema(Schema):
    hasRegex = fields.String(required=True)



