from marshmallow import fields
from neomodel import DateTimeFormatProperty
from src.Models.DataObject.v0_0_2.Date import Date, Schema


class Schema(Schema):
    startDateValue = fields.Date(required=True)
    endDateValue = fields.Date(required=True)


class Interval(Date):
    startDateValue = DateTimeFormatProperty(format="%Y-%m-%d", unique_index=True, required=True)
    endDateValue = DateTimeFormatProperty(format="%Y-%m-%d", unique_index=True, required=True)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = Schema()

        super().__init__(schema, *args, **kwargs)
