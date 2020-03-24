import json

from marshmallow import fields, validate
from neomodel import RegexProperty
from src.Models.DataObject.v0_0_2.String import Schema, String


class Schema(Schema):
    hasRegex = fields.String(required=False, validate=[
        validate.Length(0, 71), validate.Regexp('regex/[a-zA-Z]([a-zA-Z 0-9])*$', 0, error='regex invalid'),
        lambda x: x != "regex/"
    ])


class RegexString(String):
    def __init__(self, schema=None, *args, **kwargs):

        if schema is None:
            schema = Schema()

        expression = ""
        if kwargs.get("expression") is None:
            expression = 'regex/[a-zA-Z]([a-zA-Z 0-9])*$'  # TODO falta arranjar isto
        else:
            expression = json.dumps(kwargs.get("expression"))

        hasRegex = RegexProperty(
            expression=expression, unique_index=True, required=True
        )

        super().__init__(schema, *args, **kwargs)
