from marshmallow import fields
from neomodel import DateTimeFormatProperty
from src.Models.DataObject.v0_0_2.Date import Date, Schema


class Schema(Schema):
    approximateDateValue = fields.Date(required=True)


class Approximate(Date):
    approximateDateValue = DateTimeFormatProperty(format="%y-%m-%d", unique_index=True, required=True)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = Schema()

        super().__init__(schema, *args, **kwargs)
