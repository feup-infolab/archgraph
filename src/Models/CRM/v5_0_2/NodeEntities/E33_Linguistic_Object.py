from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E56_Language import E56_LanguageSchema
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import (
    E73_Information_Object,
    E73_Information_ObjectSchema)
from src.Models.CRM.v5_0_2.NodeProperties.P72_has_language import P72_has_language
from src.Models.CRM.v5_0_2.NodeProperties.P73_has_translation import P73_has_translation

from src.GCF.decorators.OntologyClass import decorator_schema

@decorator_schema
class E33_Linguistic_ObjectSchema(E73_Information_ObjectSchema):
    has_translation = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E33_Linguistic_Object.E33_Linguistic_ObjectSchema")
    )
    has_language = fields.List(fields.Nested(
        E56_LanguageSchema)
    )


class E33_Linguistic_Object(E73_Information_Object):
    has_translation = RelationshipTo(
        ".E33_Linguistic_Object.E33_Linguistic_Object",
        "P73_has_translation",
        model=P73_has_translation,
    )
    has_language = RelationshipTo(
        ".E56_Language.E56_Language", "P72_has_language", model=P72_has_language,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E33_Linguistic_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
