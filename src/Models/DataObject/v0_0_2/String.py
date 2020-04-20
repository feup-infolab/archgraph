from marshmallow import fields
from neomodel import StringProperty
from src.Models.DataObject.v0_0_2.DataObject import DataObject, DataObjectSchema


class StringSchema(DataObjectSchema):
    stringValue = fields.String(required=True)


class String(DataObject):
    stringValue = StringProperty(unique_index=True, required=True)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = StringSchema()

        super().__init__(schema, *args, **kwargs)
