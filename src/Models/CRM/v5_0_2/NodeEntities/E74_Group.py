from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor
from src.Models.CRM.v5_0_2.NodeProperties.P107_has_current_or_former_member import \
    P107_has_current_or_former_member
from src.Models.CRM.v5_0_2.NodeProperties.P151_was_formed_from import \
    P151_was_formed_from


class E74_Group(E39_Actor):
    has_current_or_former_member = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P107_has_current_or_former_member",
        model=P107_has_current_or_former_member,
    )
