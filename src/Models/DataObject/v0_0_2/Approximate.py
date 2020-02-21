from marshmallow import Schema, fields
from neomodel import DateTimeProperty

from src.Models.DataObject.v0_0_2.Date import Date


class Approximate(Date):
    approximateDateValue = DateTimeProperty(unique_index=True, required=True)


class ApproximateSchema(Schema):
    approximateDateValue = fields.Date()


approximate = Approximate()
approximate_schema = ApproximateSchema()

approximate_schema.dump(approximate)
