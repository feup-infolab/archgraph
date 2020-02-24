import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import DateTimeProperty
from src.Models.DataObject.v0_0_2.Date import Date


class Instant(Date):
    timestamp = DateTimeProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class InstantSchema(Schema):
    timestamp = fields.Date()


def getSchema():
    instant_schema = InstantSchema()
    json_schema = JSONSchema()
    json_schema.dump(instant_schema)
