from marshmallow import Schema, fields
from neomodel import DateTimeProperty

from src.Models.DataObject.v0_0_2 import SerializeClass
from src.Models.DataObject.v0_0_2.Date import Date


class IntervalSchema(Schema):
    startDateValue = fields.Date(required=True)
    endDateValue = fields.Date(required=True)


class Interval(Date):
    super(SerializeClass).__init__(IntervalSchema)
    startDateValue = DateTimeProperty(unique_index=True, required=True)
    endDateValue = DateTimeProperty(unique_index=True, required=True)




