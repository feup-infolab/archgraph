from marshmallow import Schema, fields
from neomodel import StringProperty, StructuredNode, UniqueIdProperty
from src.Models.DataObject.v0_0_2.SerializeClass import SerializeClass


class Schema(Schema):
    uid = fields.String()
    name = fields.String(required=True)


class DataObject(StructuredNode, SerializeClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()

    def __init__(self, schema=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if schema is None:
            schema = Schema()

        SerializeClass.__init__(self, schema)
        self.schema = schema
