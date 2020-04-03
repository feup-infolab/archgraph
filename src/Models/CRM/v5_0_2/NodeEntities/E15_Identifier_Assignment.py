from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import \
    E13_Attribute_Assignment
from src.Models.CRM.v5_0_2.NodeProperties.P37_assigned import P37_assigned
from src.Models.CRM.v5_0_2.NodeProperties.P38_deassigned import P38_deassigned
from src.Models.CRM.v5_0_2.NodeProperties.P142_used_constituent import \
    P142_used_constituent


class E15_Identifier_Assignment(E13_Attribute_Assignment):
    used_constituent = RelationshipTo(
        ".E90_Symbolic_Object.E90_Symbolic_Object",
        "P142_used_constituent",
        model=P142_used_constituent,
    )
    deassigned = RelationshipTo(
        ".E42_Identifier.E42_Identifier", "P38_deassigned", model=P38_deassigned,
    )
    assigned = RelationshipTo(
        ".E42_Identifier.E42_Identifier", "P37_assigned", model=P37_assigned,
    )
