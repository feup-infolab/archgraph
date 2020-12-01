from marshmallow import fields, Schema
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import (
    E73_Information_Object,
    E73_Information_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P68_foresees_use_of import P68_foresees_use_of
from src.Models.CRM.v5_0_2.NodeProperties.P69_has_association_with import (
    P69_has_association_with,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E29_Design_or_ProcedureSchema(E73_Information_ObjectSchema):
    has_association_with = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E29_Design_or_Procedure.E29_Design_or_ProcedureSchema"
        )
    )
    foresees_use_of = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E57_Material.E57_MaterialSchema"
        )
    )


class E29_Design_or_Procedure(E73_Information_Object):
    has_association_with = RelationshipTo(
        ".E29_Design_or_Procedure.E29_Design_or_Procedure",
        "P69_has_association_with",
        model=P69_has_association_with,
    )
    foresees_use_of = RelationshipTo(
        ".E57_Material.E57_Material", "P68_foresees_use_of", model=P68_foresees_use_of,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E29_Design_or_ProcedureSchema()

        super().__init__(schema, *args, **kwargs)
