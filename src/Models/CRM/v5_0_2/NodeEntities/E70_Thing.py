from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import \
    E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P16_used_specific_object import \
    P16_used_specific_object
from src.Models.CRM.v5_0_2.NodeProperties.P43_has_dimension import \
    P43_has_dimension
from src.Models.CRM.v5_0_2.NodeProperties.P101_had_as_general_use import \
    P101_had_as_general_use
from src.Models.CRM.v5_0_2.NodeProperties.P130_shows_features_of import \
    P130_shows_features_of


class E70_Thing(E77_Persistent_Item):
    showsFeaturesOf = RelationshipTo(
        ".E70_Thing.E70_Thing", "P130_shows_features_of", model=P130_shows_features_of
    )
    had_as_general_use = RelationshipTo(
        ".E55_Type.E55_Type", "P101_had_as_general_use", model=P101_had_as_general_use
    )
    has_dimension = RelationshipTo(
        ".E54_Dimension.E54_Dimension", "P43_has_dimension", model=P43_has_dimension
    )
