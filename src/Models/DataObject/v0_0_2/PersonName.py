from marshmallow import fields
from neomodel import StringProperty
from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString
from src.Models.DataObject.v0_0_2.DataObject import DataObject

#config.DATABASE_URL = "bolt://neo4j:password@localhost:7687"
# from src.GCF.utils.db import clean_database
# clean_database()


class PersonNameSchema(DataObject):
    name = fields.String(required=True)


class PersonName(AuthorityString):
    name = StringProperty(unique_index=True, required=True)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = PersonNameSchema()

        super().__init__(schema, *args, **kwargs)
        self.list.append(self.name)


#a = PersonName(name="new").save()
