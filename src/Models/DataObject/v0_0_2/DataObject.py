from marshmallow import Schema, fields
from neomodel import StringProperty, StructuredNode, UniqueIdProperty
from src.Models.DataObject.v0_0_2.SuperClass import SuperClass


class DataObjectSchema(Schema):
    uid = fields.String()
    name = fields.String(required=True)


class DataObject(StructuredNode, SuperClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()

    def __init__(self, schema=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if schema is None:
            schema = DataObjectSchema()

        SuperClass.__init__(self, schema)


var = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "definitions": {
        "PersonNameSchema": {
            "properties": {
                "name": {"title": "name", "type": "string"},
                "person_name": {"title": "person_name", "type": "string"},
                "stringValue": {"title": "stringValue", "type": "string"},
                "uid": {"title": "uid", "type": "string"},
            },
            "required": ["name", "person_name", "stringValue"],
            "type": "object",
            "additionalProperties": False,
        }
    },
    "$ref": "#/definitions/PersonNameSchema",
}
