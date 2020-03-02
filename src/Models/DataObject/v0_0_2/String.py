import json
from marshmallow import Schema, fields

from neomodel import StringProperty
from src.Models.DataObject.v0_0_2.DataObject import DataObject


@has_json_schema
class String(DataObject):
    stringValue = StringProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class StringSchema(Schema):
    stringValue = fields.String(required=True)
