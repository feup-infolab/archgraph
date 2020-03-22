from marshmallow import Schema, fields
from neomodel import StringProperty, StructuredNode, UniqueIdProperty
from src.Models.DataObject.v0_0_2.SuperClass import SuperClass


class Schema(Schema):
    uid = fields.String()
    name = fields.String(required=True)


class DataObject(StructuredNode, SuperClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()

    def __init__(self, schema=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if schema is None:
            schema = Schema()

        SuperClass.__init__(self, schema)

    def merge_node(self, updated_node):
        merged_node = {**self.decodeJSON(), **updated_node}
        for attr, value in merged_node.items():
            get_attr = getattr(self, attr)
            if get_attr != value:
                setattr(self, attr, value)
        self.save()
        return
