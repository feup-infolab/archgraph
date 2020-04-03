from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import \
    E63_Beggining_of_Existence
from src.Models.CRM.v5_0_2.NodeProperties.P94_has_created import \
    P94_has_created


class E65_Creation(E7_Activity, E63_Beggining_of_Existence):
    has_created = RelationshipTo(
        ".E28_Conceptual_Object.E28_Conceptual_Object",
        "P94_has_created",
        model=P94_has_created,
    )
