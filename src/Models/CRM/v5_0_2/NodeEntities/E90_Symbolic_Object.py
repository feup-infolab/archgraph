from marshmallow import Schema, fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import (
    E28_Conceptual_Object,
    E28_Conceptual_ObjectSchema)
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import E72_Legal_Object, E72_Legal_ObjectSchema
from src.Models.CRM.v5_0_2.NodeProperties.P106_is_composed_of import P106_is_composed_of


#todo
class E90_Symbolic_ObjectSchema(E28_Conceptual_ObjectSchema):
    P106_is_composed_of = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object.E90_Symbolic_ObjectSchema")
    )


class E90_Symbolic_Object(E72_Legal_Object, E28_Conceptual_Object):
    P106_is_composed_of = RelationshipTo(
        ".E90_Symbolic_Object.E90_Symbolic_Object",
        "P106_is_composed_of",
        model=P106_is_composed_of,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E90_Symbolic_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
