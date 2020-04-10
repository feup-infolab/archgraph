from neomodel import RelationshipFrom
from src.Models.ArchOnto.v0_1.NodeProperties.ARP8_upper_level import \
    ARP8_upper_level
from src.Models.ArchOnto.v0_1.NodeProperties.ARP9_lower_level import \
    ARP9_lower_level
from src.Models.ArchOnto.v0_1.NodeProperties.ARP12_has_level_of_description import \
    ARP12_has_level_of_description
from src.Models.CRM.v5_0_2.NodeEntities.E22_Human_Made_Object import \
    E22_Human_Made_Object
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type


class ARE1_Level_of_Description(E55_Type):
    upper_level = RelationshipFrom(
        ".ARE1_Level_of_Description.ARE1_Level_of_Description",
        "ARP8_upper_level",
        model=ARP8_upper_level,
    )
    lower_level = RelationshipFrom(
        ".ARE1_Level_of_Description.ARE1_Level_of_Description", "ARP9_lower_level", model=ARP9_lower_level
    )
    has_level_of_description = RelationshipFrom(
        E22_Human_Made_Object, "ARP12_has_level_of_description", model=ARP12_has_level_of_description
    )