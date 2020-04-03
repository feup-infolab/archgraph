from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import \
    E77_Persistent_Item
from src.Models.CRM.v5_0_2.NodeProperties.P74_has_current_or_former_residence import \
    P74_has_current_or_former_residence
from src.Models.CRM.v5_0_2.NodeProperties.P75_possesses import P75_possesses


class E39_Actor(E77_Persistent_Item):
    has_current_or_former_residence = RelationshipTo(
        ".E53_Place.E53_Place",
        "P74_has_current_or_former_residence",
        model=P74_has_current_or_former_residence,
    )
    possesses = RelationshipTo(
        ".E30_Right.E30_Right", "P75_possesses", model=P75_possesses
    )
