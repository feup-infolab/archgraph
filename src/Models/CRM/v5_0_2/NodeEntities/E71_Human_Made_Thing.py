from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P19_was_intended_use_of import \
    P19_was_intended_use_of
from src.Models.CRM.v5_0_2.NodeProperties.P102_has_title import P102_has_title


class E71_Human_Made_Thing(E70_Thing):
    has_title = RelationshipFrom(
        ".E35_Title.E35_Title", "P46_has_title", model=P102_has_title
    )
    was_intended_use_of = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P19_was_intended_use_of",
        model=P19_was_intended_use_of,
    )
