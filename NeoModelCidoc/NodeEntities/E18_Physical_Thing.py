from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from NodeEntities.E72_Legal_Object import E72_Legal_Object
from NodeEntities.StructuredRelCl import StructuredRelCl


class P46_is_composed_of(StructuredRelCl):
    pass


class P8_took_place_on_or_within(StructuredRelCl):
    pass


class P13_destroyed(StructuredRelCl):
    pass


class E18_Physical_Thing(E72_Legal_Object):
    isComposedOf = RelationshipFrom('E18_Physical_Thing', 'P46_is_composed_of', model=P46_is_composed_of)
    took_place_on_or_within = RelationshipFrom('E4_Period', 'P8_took_place_on_or_within', model=P8_took_place_on_or_within)
    destroyed = RelationshipFrom('E6_Destruction', 'P13_destroyed', model=P13_destroyed)
