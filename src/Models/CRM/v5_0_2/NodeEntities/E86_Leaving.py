from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P145_separated import P145_separated
from src.Models.CRM.v5_0_2.NodeProperties.P146_separated_from import P146_separated_from


class E86_Leaving(E7_Activity):
    separated = RelationshipTo(
        ".E39_Actor.E39_Actor", "P145_separated_from", model=P145_separated
    )
    separated_from = RelationshipTo(
        ".E74_Group.E74_Group", "P146_separated_from", model=P146_separated_from
    )
