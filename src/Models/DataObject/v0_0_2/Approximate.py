import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import DateTimeProperty

from src.Models.DataObject.v0_0_2 import SerializeClass
from src.Models.DataObject.v0_0_2.Date import Date


class ApproximateSchema(Schema):
    approximateDateValue = fields.Date(required=True)


class Approximate(Date):
    super(SerializeClass).__init__(ApproximateSchema)
    approximateDateValue = DateTimeProperty(unique_index=True, required=True)


