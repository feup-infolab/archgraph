from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema
from src.Models.CRM.v5_0_2.NodeProperties.P187_has_production_plan import (
    P187_has_production_plan,
)
from src.Models.CRM.v5_0_2.NodeProperties.P188_requires_production_tool import (
    P188_requires_production_tool,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E99_Product_TypeSchema(E55_TypeSchema):
    requires_production_tool = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object.E19_Physical_ObjectSchema"
        )
    )
    has_production_plan = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E29_Design_or_Procedure.E29_Design_or_ProcedureSchema"
        )
    )


class E99_Product_Type(E55_Type):
    requires_production_tool = RelationshipTo(
        ".E19_Physical_Object.E19_Physical_Object",
        "P188_requires_production_tool",
        model=P188_requires_production_tool,
    )
    has_production_plan = RelationshipTo(
        ".E29_Design_or_Procedure.E29_Design_or_Procedure",
        "P187_has_production_plan",
        model=P187_has_production_plan,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E99_Product_TypeSchema()

        super().__init__(schema, *args, **kwargs)
