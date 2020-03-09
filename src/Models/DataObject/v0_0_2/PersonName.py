import json

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from neomodel import StringProperty

from src.Models.DataObject.v0_0_2 import SerializeClass
from src.Models.DataObject.v0_0_2.AuthorityString import AuthorityString


class PersonNameSchema(Schema):
    name = fields.String(required=True)


class PersonName(AuthorityString):
    super(SerializeClass).__init__(PersonNameSchema)
    name = StringProperty(unique_index=True, required=True)


