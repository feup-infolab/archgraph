import json
from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import RegexProperty
from src.Models.DataObject.v0_0_2.String import String


class RegexString(String):
    hasRegex = RegexProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class RegexStringSchema(Schema):
    hasRegex = fields.String()


def getSchema():
    regex_string_schema = RegexStringSchema()
    json_schema = JSONSchema()
    json_schema.dump(regex_string_schema)
