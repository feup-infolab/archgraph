from neomodel import (DateTimeProperty)
from src.Models.DataObject.v0_0_2.Date import Date
from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema


class Instant(Date):
    timestamp = DateTimeProperty(unique_index=True, required=True)


class InstantSchema(Schema):
    timestamp = fields.Date()


instant_schema = InstantSchema()

json_schema = JSONSchema()
json_schema.dump(instant_schema)
