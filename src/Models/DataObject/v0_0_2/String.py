from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import StringProperty
from src.Models.DataObject.v0_0_2.DataObject import DataObject


class String(DataObject):
    stringValue = StringProperty(unique_index=True, required=True)


class StringSchema(Schema):
    stringValue = fields.String()


string_schema = StringSchema()

json_schema = JSONSchema()
json_schema.dump(string_schema)
