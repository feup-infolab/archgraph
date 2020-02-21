from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import RegexProperty

from src.Models.DataObject.v0_0_2.String import String


class RegexString(String):
    hasRegex = RegexProperty(unique_index=True, required=True)


class RegexStringSchema(Schema):
    hasRegex = fields.String()


regex_string_schema = RegexStringSchema()

json_schema = JSONSchema()
json_schema.dump(regex_string_schema)
