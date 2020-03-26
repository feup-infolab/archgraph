from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period
from src.Models.CRM.v5_0_2.NodeProperties.P20_had_specific_purpose import \
    P20_had_specific_purpose


class E5_Event(E4_Period):
    had_specific_purpose = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P20_had_specific_purpose",
        model=P20_had_specific_purpose,
    )
