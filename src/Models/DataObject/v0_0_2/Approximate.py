import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import DateTimeProperty

from src.Models.DataObject.v0_0_2.Date import Date


class Approximate(Date):
    approximateDateValue = DateTimeProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def getSchema(self):
        approximate_schema = ApproximateSchema()
        json_schema = JSONSchema()
        return json_schema.dump(approximate_schema)


class ApproximateSchema(Schema):
    approximateDateValue = fields.Date(required=True)
