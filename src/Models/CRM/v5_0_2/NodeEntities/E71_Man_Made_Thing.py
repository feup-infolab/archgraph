from neomodel import (RelationshipTo)

from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P102_has_title import P102_has_title


class E71_Man_Made_Thing(E70_Thing):
    has_title = RelationshipTo(
        ".E35_Title.E35_Title", "P46_has_title", model=P102_has_title,
    )
