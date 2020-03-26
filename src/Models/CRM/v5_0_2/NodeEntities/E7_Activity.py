from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from ..NodeEntities.E5_Event import E5_Event
from ..NodeProperties.P134_continued import P134_continued


class E7_Activity(E5_Event):
    continued = RelationshipFrom(
        ".E7_Activity.E7_Activity", "P134_continued", model=P134_continued
    )
