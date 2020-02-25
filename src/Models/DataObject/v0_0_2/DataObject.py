import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class DataObject(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def getSchema(self):
        data_object_schema = DataObjectSchema()
        json_schema = JSONSchema()
        return json_schema.dump(data_object_schema)


class DataObjectSchema(Schema):
    uid = fields.String()
    name = fields.String(required=True)



