from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P25_moved import P25_moved
from src.Models.CRM.v5_0_2.NodeProperties.P26_moved_to import P26_moved_to
from src.Models.CRM.v5_0_2.NodeProperties.P27_moved_from import P27_moved_from


class E9_Move(E7_Activity):
    moved_to = RelationshipTo(
        ".E53_Place.E53_Place", "P26_moved_to", model=P26_moved_to
    )
    moved_from = RelationshipTo(
        ".E53_Place.E53_Place", "P27_moved_from", model=P27_moved_from
    )
    moved = RelationshipTo(
        ".E19_Physical_Object.E19_Physical_Object", "P25_moved", model=P25_moved
    )
