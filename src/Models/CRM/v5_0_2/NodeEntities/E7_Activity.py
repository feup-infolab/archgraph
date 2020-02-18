from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
    RelationshipFrom,
)

from ..NodeEntities.E5_Event import E5_Event
from ..NodeProperties.PC14_Carried_Out_By import PC14_Carried_Out_By


class E7_Activity(E5_Event):
    carried_out_by = RelationshipTo(
        "E7_Activity", "P14_carried_out_by", model=PC14_Carried_Out_By
    )
