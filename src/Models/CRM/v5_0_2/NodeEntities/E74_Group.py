from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor
from src.Models.CRM.v5_0_2.NodeProperties.P95_has_formed import P95_has_formed
from src.Models.CRM.v5_0_2.NodeProperties.P99_dissolved import P99_dissolved


class E74_Group(E39_Actor):
    has_formed = RelationshipFrom(
        ".E66_Formation.E66_Formation",
        "P95_has_formed",
        model=P95_has_formed
    )
    dissolved = RelationshipFrom(
        ".E68_Dissolution.E68_Dissolution",
        "P99_dissolved",
        model=P99_dissolved
    )
