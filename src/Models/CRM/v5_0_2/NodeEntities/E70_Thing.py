from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import \
    E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P130_shows_features_of import \
    P130_shows_features_of
from src.Models.CRM.v5_0_2.NodeProperties.P16_used_specific_object import P16_used_specific_object


class E70_Thing(E77_Persistent_Item):
    showsFeaturesOf = RelationshipFrom(
        ".E70_Thing.E70_Thing", "P130_shows_features_of", model=P130_shows_features_of
    )
    used_specific_object = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P16_used_specific_object",
        model=P16_used_specific_object
    )
