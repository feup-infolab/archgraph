import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import DateTimeProperty
from src.Models.DataObject.v0_0_2.Date import Date


class InstantSchema(Schema):
    timestamp = fields.Date(required=True)


class Instant(Date):
    timestamp = DateTimeProperty(unique_index=True, required=True)



