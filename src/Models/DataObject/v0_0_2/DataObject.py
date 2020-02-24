import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class DataObject(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DataObjectSchema(Schema):
    uid = fields.String()
    name = fields.String()


def getSchema():
    data_object_schema = DataObjectSchema()
    json_schema = JSONSchema()
    json_schema.dump(data_object_schema)
    # print(json_schema.dump(data_object_schema))
