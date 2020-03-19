from marshmallow import fields
from neomodel import DateTimeProperty
from src.Models.DataObject.v0_0_2.Date import Date, DateSchema


class InstantSchema(DateSchema):
    timestamp = fields.Date(required=True)


class Instant(Date):
    timestamp = DateTimeProperty(unique_index=True, required=True)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = InstantSchema()

        super().__init__(schema, *args, **kwargs)
        self.list.append(self.timestamp)
