from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import StringProperty
import json
from src.Models.DataObject.v0_0_2.DataObject import DataObject


class String(DataObject):
    stringValue = StringProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class StringSchema(Schema):
    stringValue = fields.String()


def getSchema():
    string_schema = StringSchema()
    json_schema = JSONSchema()
    return json_schema.dump(string_schema)
