from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)
from NodeEntities.E77_Persistent_Item import E77_Persistent_Item


class E70_Thing(StructuredNode, E77_Persistent_Item):
    pass
