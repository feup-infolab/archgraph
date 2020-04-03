from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeProperties.P187_has_production_plan import \
    P187_has_production_plan
from src.Models.CRM.v5_0_2.NodeProperties.P188_requires_production_tool import \
    P188_requires_production_tool


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
