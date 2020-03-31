from marshmallow import fields
from neomodel import StringProperty
from src.Models.DataObject.v0_0_2.AuthorityString import (
    AuthorityString, AuthorityStringSchema)


class PersonNameSchema(AuthorityStringSchema):
    person_name = fields.String(required=True)


class PersonName(AuthorityString):
    person_name = StringProperty(unique_index=True, required=True)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = PersonNameSchema()

        super().__init__(schema, *args, **kwargs)
