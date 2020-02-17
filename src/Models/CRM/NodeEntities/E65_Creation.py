from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
)
from NodeEntities.E7_Activity import E7_Activity
from NodeEntities.E63_Beggining_of_Existence import E63_Beggining_of_Existence


class E65_Creation(E7_Activity, E63_Beggining_of_Existence):
    pass
