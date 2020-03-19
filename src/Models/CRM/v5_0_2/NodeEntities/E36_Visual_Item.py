from neomodel import RelationshipTo, StructuredRel, RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import \
    E73_Information_Object
from src.Models.CRM.v5_0_2.NodeProperties.P138_represents import P138_represents


class P65_shows_visual_item(StructuredRel):
    pass


class E36_Visual_Item(E73_Information_Object):
    showsVisualItem = RelationshipTo(
        ".E24_Physical_Man_Made_Thing.E24_Physical_Man_Made_Thing",
        "P65_shows_visual_item",
        model=P65_shows_visual_item)
    represents = RelationshipFrom(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P138_represents",
        model=P138_represents
    )
