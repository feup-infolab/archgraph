from marshmallow import Schema, fields
from neomodel import RelationshipTo
from .E28_Conceptual_Object import E28_Conceptual_Object, E28_Conceptual_ObjectSchema
from ..NodeProperties.P127_has_broader_term import P127_has_broader_term
from ..NodeProperties.P150_defines_typical_parts_of import \
    P150_defines_typical_parts_of


class E55_TypeSchema(E28_Conceptual_ObjectSchema):
    P127_has_broader_term = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema"))
    P150_defines_typical_parts_of = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema"))


class E55_Type(E28_Conceptual_Object):
    P127_has_broader_term = RelationshipTo(
        ".E55_Type.E55_Type", "P127_has_broader_term", model=P127_has_broader_term
    )
    P150_defines_typical_parts_of = RelationshipTo(
        ".E55_Type.E55_Type",
        "P150_defines_typical_parts_of",
        model=P150_defines_typical_parts_of,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E55_TypeSchema()

        super().__init__(schema, *args, **kwargs)
