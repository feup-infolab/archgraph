from marshmallow import Schema, fields
from neomodel import StringProperty, StructuredNode, UniqueIdProperty
from src.Models.DataObject.v0_0_2.SerializeClass import SerializeClass

# config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
# from src.GCF.utils.db import clean_database
# clean_database()


class DataObjectSchema(Schema):
    uid = fields.String()
    name = fields.String(required=True)


class DataObject(StructuredNode, SerializeClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()

    def __init__(self, schema=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if schema is None:
            schema = DataObjectSchema()

        SerializeClass.__init__(self, schema)
        self.schema = schema
        self.list.extend([self.uid, self.name])


# ola =DataObject(name="ola").save()
# ola.getSchema()
# print(ola.toJSON())
# ola.nodes.get(name="ola")
