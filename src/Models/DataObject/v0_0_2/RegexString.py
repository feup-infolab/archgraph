import json

from marshmallow import fields, validate
from neomodel import RegexProperty
from src.Models.DataObject.v0_0_2.String import String, StringSchema
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class RegexStringSchema(StringSchema):
    hasRegex = fields.String(
        required=False,
        validate=[
            validate.Length(0, 71),
            validate.Regexp("regex/[a-zA-Z]([a-zA-Z 0-9])*$", 0, error="regex invalid"),
            lambda x: x != "regex/",
        ],
    )


class RegexString(String):
    def __init__(self, schema=None, *args, **kwargs):

        if schema is None:
            schema = RegexStringSchema()

        expression = ""
        if kwargs.get("expression") is None:
            # todo falta arranjar isto
            expression = "regex/[a-zA-Z]([a-zA-Z 0-9])*$"
        else:
            expression = json.dumps(kwargs.get("expression"))

        hasRegex = RegexProperty(
            expression=expression, unique_index=True, required=True
        )

        super().__init__(schema, *args, **kwargs)
