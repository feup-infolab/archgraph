from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E65_Creation import E65_Creation
from src.Models.CRM.v5_0_2.NodeProperties.P135_created_type import \
    P135_created_type
from src.Models.CRM.v5_0_2.NodeProperties.P136_was_based_on import \
    P136_was_based_on


class E83_Type_Creation(E65_Creation):
    was_based_on = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P136_was_based_on", model=P136_was_based_on,
    )
    created_type = RelationshipTo(
        ".E55_Type.E55_Type", "P135_created_type", model=P135_created_type,
    )
