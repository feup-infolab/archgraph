from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E71_Human_Made_Thing import \
    E71_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P110_augmented import P110_augmented
from src.Models.CRM.v5_0_2.NodeProperties.P112_diminished import \
    P112_diminished
from src.Models.CRM.v5_0_2.NodeProperties.P65_shows_visual_item import P65_shows_visual_item


class E24_Physical_Human_Made_Thing(E18_Physical_Thing, E71_Human_Made_Thing):
    showsVisualItem = RelationshipFrom(
        ".E36_Visual_Item.E36_Visual_Item",
        "P65_shows_visual_item",
        model=P65_shows_visual_item,
    )

    augmented = RelationshipFrom(
        ".E79_Part_Addition.E79_Part_Addition", "P110_augmented", model=P110_augmented
    )
    diminished = RelationshipFrom(
        ".E80_Part_Removal.E80_Part_Removal", "P112_diminished", model=P112_diminished
    )
