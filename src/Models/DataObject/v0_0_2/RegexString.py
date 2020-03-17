import json

from marshmallow import fields
from neomodel import RegexProperty
from src.Models.DataObject.v0_0_2.String import String, StringSchema


class RegexStringSchema(StringSchema):
    hasRegex = fields.String(required=True)


class RegexString(String):
    def __init__(self, schema=None, *args, **kwargs):

        if schema is None:
            schema = RegexStringSchema()

        expression = ""
        if kwargs.get("expression") is None:
            expression = "r'dw"  # TODO falta arranjar isto
        else:
            expression = json.dumps(kwargs.get("expression"))

        hasRegex = RegexProperty(
            expression=expression, unique_index=True, required=True
        )
        schema = RegexStringSchema()

        super().__init__(schema, *args, **kwargs)
