from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import \
    E73_Information_Object
from src.Models.CRM.v5_0_2.NodeProperties.StructuredRelCl import \
    StructuredRelCl


class P65_shows_visual_item(StructuredRelCl):
    pass


class E36_Visual_Item(E73_Information_Object):

    showsVisualItem = RelationshipTo(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing",
        "P65_shows_visual_item",
        model=P65_shows_visual_item,
    )
