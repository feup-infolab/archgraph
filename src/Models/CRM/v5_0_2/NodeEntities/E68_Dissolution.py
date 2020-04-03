from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import \
    E64_End_of_Existence
from src.Models.CRM.v5_0_2.NodeProperties.P99_dissolved import P99_dissolved


class E68_Dissolution(E64_End_of_Existence):
    dissolved = RelationshipTo(
        ".E74_Group.E74_Group", "P99_dissolved", model=P99_dissolved
    )
