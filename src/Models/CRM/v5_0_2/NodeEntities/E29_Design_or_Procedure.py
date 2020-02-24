from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import \
    E73_Information_Object
from src.Models.CRM.v5_0_2.NodeProperties.P33_used_specific_technique import P33_used_specific_technique


class E29_Design_or_Procedure(E73_Information_Object):
    used_specific_technique = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P33_used_specific_technique",
        model=P33_used_specific_technique
    )
