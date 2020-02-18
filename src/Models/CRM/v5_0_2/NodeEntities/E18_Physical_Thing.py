from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import E72_Legal_Object
from neomodel import StructuredRel


class P46_is_composed_of(StructuredRel):
    pass


class P8_took_place_on_or_within(StructuredRel):
    pass


class P13_destroyed(StructuredRel):
    pass


class E18_Physical_Thing(E72_Legal_Object):
    isComposedOf = RelationshipFrom(
        "E18_Physical_Thing", "P46_is_composed_of", model=P46_is_composed_of
    )
    took_place_on_or_within = RelationshipFrom(
        "E4_Period", "P8_took_place_on_or_within", model=P8_took_place_on_or_within
    )
    destroyed = RelationshipFrom("E6_Destruction", "P13_destroyed", model=P13_destroyed)
