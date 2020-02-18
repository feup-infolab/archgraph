from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import E77_Persistent_Item
from neomodel import StructuredRel


class P130_shows_features_of(StructuredRel):
    pass


class E70_Thing(E77_Persistent_Item):
    showsFeaturesOf = RelationshipFrom(
        "E70_Thing", "P130_shows_features_of", model=P130_shows_features_of
    )
