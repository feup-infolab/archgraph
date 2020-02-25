from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor
from src.Models.CRM.v5_0_2.NodeProperties.P144_joined_with import P144_joined_with
from src.Models.CRM.v5_0_2.NodeProperties.P146_separated_from import P146_separated_from
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
    joined_with = RelationshipFrom(
        ".E85_Joining.E85_Joining",
        "P144_joined_with",
        model=P144_joined_with
    )
    separated_from = RelationshipFrom(
        ".E86_Leaving.E86_Leaving",
        "P146_separated_from",
        model=P146_separated_from
    )
