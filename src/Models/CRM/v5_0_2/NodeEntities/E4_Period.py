from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
    RelationshipFrom,
)
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity
from neomodel import StructuredRel


class P9_consists_of(StructuredRel):
    pass


class E4_Period(E2_Temporal_Entity):
    consists_of = RelationshipFrom("E4_Period", "P9_consists_of", model=P9_consists_of)
