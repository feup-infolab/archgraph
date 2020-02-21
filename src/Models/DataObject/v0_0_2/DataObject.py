from neomodel import (StructuredNode, StringProperty)
from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema


class DataObject(StructuredNode):
    name = StringProperty(unique_index=True, required=True)


class DataObjectSchema(Schema):
    name = fields.String()


data_object_schema = DataObjectSchema()

json_schema = JSONSchema()
json_schema.dump(data_object_schema)
#print(json_schema.dump(data_object_schema))
