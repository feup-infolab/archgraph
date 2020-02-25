from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import StringProperty
import json

from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString


class PersonName(AuthorityString):
    name = StringProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def getSchema(self):
        person_name_schema = PersonNameSchema()
        json_schema = JSONSchema()
        return json_schema.dump(person_name_schema)


class PersonNameSchema(Schema):
    name = fields.String(required=True)



