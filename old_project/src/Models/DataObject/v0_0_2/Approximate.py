from marshmallow import fields
from neomodel import DateTimeFormatProperty
from src.Models.DataObject.v0_0_2.Date import Date, DateSchema
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class ApproximateSchema(DateSchema):
    approximateDateValue = fields.Date(required=True)


class Approximate(Date):
    approximateDateValue = DateTimeFormatProperty(
        format="%Y-%m-%d", unique_index=True, required=True
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ApproximateSchema()

        super().__init__(schema, *args, **kwargs)
