import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import DateTimeProperty

from src.Models.DataObject.v0_0_2.Date import Date


class Interval(Date):
    startDateValue = DateTimeProperty(unique_index=True, required=True)
    endDateValue = DateTimeProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def getSchema(self):
        interval_schema = IntervalSchema()
        json_schema = JSONSchema()
        return json_schema.dump(interval_schema)


class IntervalSchema(Schema):
    startDateValue = fields.Date(required=True)
    endDateValue = fields.Date(required=True)
