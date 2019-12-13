from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from NodeEntities.E77_Persistent_Item import E77_Persistent_Item
from NodeProperties.StructuredRelCl import StructuredRelCl


class P130_shows_features_of(StructuredRelCl):
    pass


class E70_Thing(E77_Persistent_Item):
    showsFeaturesOf = RelationshipFrom('E70_Thing', 'P130_shows_features_of', model=P130_shows_features_of)
