from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import \
    E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P130_shows_features_of import \
    P130_shows_features_of


class E70_Thing(E77_Persistent_Item):
    showsFeaturesOf = RelationshipFrom(
        ".E70_Thing.E70_Thing", "P130_shows_features_of", model=P130_shows_features_of
    )
