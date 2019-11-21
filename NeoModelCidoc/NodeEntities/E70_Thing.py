from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from NodeEntities.E77_Persistent_Item import E77_Persistent_Item


class E70_Thing(E77_Persistent_Item):
    showsFeaturesOf = RelationshipFrom('E70_Thing', 'P130_shows_features_of')
