from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P19_was_intended_use_of import \
    P19_was_intended_use_of
from src.Models.CRM.v5_0_2.NodeProperties.P102_has_title import P102_has_title
from src.Models.CRM.v5_0_2.NodeProperties.P103_was_intended_for import \
    P103_was_intended_for


class E71_Human_Made_Thing(E70_Thing):
    was_intended_for = RelationshipTo(
        ".E55_Type.E55_Type", "P103_was_intended_for", model=P103_was_intended_for,
    )
    has_title = RelationshipTo(
        ".E35_Title.E35_Title", "P102_has_title", model=P102_has_title,
    )
