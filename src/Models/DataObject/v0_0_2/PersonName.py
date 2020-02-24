from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import StringProperty
import json

from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString


class PersonName(AuthorityString):
    name = StringProperty(unique_index=True, required=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class PersonNameSchema(Schema):
    name = fields.String()


def getSchema():
    person_name_schema = PersonNameSchema()
    json_schema = JSONSchema()
    json_schema.dump(person_name_schema)
