from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import DateTimeProperty
from src.Models.DataObject.v0_0_2.Date import Date


class Interval(Date):
    startDateValue = DateTimeProperty(unique_index=True, required=True)
    endDateValue = DateTimeProperty(unique_index=True, required=True)


class IntervalSchema(Schema):
    startDateValue = fields.Date()
    endDateValue = fields.Date()


interval_schema = IntervalSchema()

json_schema = JSONSchema()
json_schema.dump(interval_schema)
