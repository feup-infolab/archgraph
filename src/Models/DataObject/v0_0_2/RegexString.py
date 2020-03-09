from marshmallow import fields
from neomodel import RegexProperty
from src.Models.DataObject.v0_0_2.DataObject import DataObject
from src.Models.DataObject.v0_0_2.String import String


class RegexStringSchema(DataObject):
    hasRegex = fields.String(required=True)


class RegexString(String):
    def __init__(self, expression=None, schema=None, *args, **kwargs):
        hasRegex = RegexProperty(
            expression=expression, unique_index=True, required=True
        )

        if schema is None:
            schema = RegexStringSchema(hasRegex=expression)

        super().__init__(schema, *args, **kwargs)
        self.list.append(hasRegex)


# config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
# a = RegexString(expression=r'dw', name="new", stringValue="ola").save()
# print(a.toJSON())
# print(a.getSchema())
