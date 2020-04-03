from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import \
    E13_Attribute_Assignment
from src.Models.CRM.v5_0_2.NodeProperties.P34_concerned import P34_concerned
from src.Models.CRM.v5_0_2.NodeProperties.P35_has_identified import \
    P35_has_identified


class E14_Condition_Assessment(E13_Attribute_Assignment):
    has_identified = RelationshipTo(
        ".E3_Condition_State.E3_Condition_State",
        "P35_has_identified",
        model=P35_has_identified,
    )
    concerned = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing", "P34_concerned", model=P34_concerned,
    )
