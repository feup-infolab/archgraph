import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import RegexProperty

from src.Models.DataObject.v0_0_2 import SerializeClass
from src.Models.DataObject.v0_0_2.String import String


class RegexStringSchema(Schema):
    hasRegex = fields.String(required=True)


class RegexString(String, SerializeClass):
    super(SerializeClass).__init__(RegexStringSchema)
    hasRegex = RegexProperty(unique_index=True, required=True)





