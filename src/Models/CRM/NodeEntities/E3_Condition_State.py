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


class P5_consists_of(StructuredRelCl):
    pass


class E3_Condition_State(E2_Temporal_Entity):
    consists_of = RelationshipFrom(
        "E3_Condition_State", "P5_consists_of", cardinality=One, model=P5_consists_of
    )
