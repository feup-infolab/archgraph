from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, StructuredRel)
from NodeEntities.E73_Information_Object import E73_Information_Object
from NodeEntities.StructuredRelCl import StructuredRelCl


class P65_shows_visual_item(StructuredRelCl):
    pass


class E36_Visual_Item(E73_Information_Object):
    showsVisualItem = RelationshipTo('E24_Physical_Man_Made_Thing', 'P65_shows_visual_item', model=P65_shows_visual_item)



