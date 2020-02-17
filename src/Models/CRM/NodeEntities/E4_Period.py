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
from NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P9_consists_of(StructuredRelCl):
    pass


class E4_Period(E2_Temporal_Entity):
    consists_of = RelationshipFrom("E4_Period", "P9_consists_of", model=P9_consists_of)
