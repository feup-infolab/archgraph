
from marshmallow import Schema, fields
from neomodel import StringProperty, StructuredNode, UniqueIdProperty
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.DataObject.v0_0_2.SuperClass import SuperClass

@decorator_schema
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



