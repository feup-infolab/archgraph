import json

from marshmallow import Schema, fields
from neomodel import DateTimeProperty
from src.Models.DataObject.v0_0_2.Date import Date


class Approximate(Date):
    approximateDateValue = DateTimeProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class ApproximateSchema(Schema):
    approximateDateValue = fields.Date()


def getSchema():
    approximate = Approximate()
    approximate_schema = ApproximateSchema()
    approximate_schema.dump(approximate)
