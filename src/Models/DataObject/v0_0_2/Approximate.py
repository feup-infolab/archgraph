
from marshmallow import fields
from neomodel import DateTimeProperty, config
from src.Models.DataObject.v0_0_2.Date import Date, DateSchema

config.DATABASE_URL = "bolt://neo4j:password@localhost:7687"


class ApproximateSchema(DateSchema):
    approximateDateValue = fields.Date(required=True)


class Approximate(Date):
    approximateDateValue = DateTimeProperty(unique_index=True, required=True)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ApproximateSchema()

        super().__init__(schema, *args, **kwargs)
        self.list.append(self.approximateDateValue.__str__())


# print(ApproximateSchema())
# datetime_object = datetime.datetime(2020, 5, 17)
# print(datetime_object)
# a = Approximate(name="name", approximateDateValue=datetime_object, ).save()
# print(a.toJSON())
# print(a.getSchema())
