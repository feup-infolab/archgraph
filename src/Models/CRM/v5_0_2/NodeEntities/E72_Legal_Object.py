from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P104_is_subject_to import \
    P104_is_subject_to
from src.Models.CRM.v5_0_2.NodeProperties.P105_right_held_by import \
    P105_right_held_by


class E72_Legal_Object(E70_Thing):
    is_subject_to = RelationshipTo(
        ".E30_Right.E30_Right", "P104_is_subject_to", model=P104_is_subject_to,
    )
    right_held_by = RelationshipTo(
        ".E39_Actor.E39_Actor", "P105_right_held_by", model=P105_right_held_by,
    )
