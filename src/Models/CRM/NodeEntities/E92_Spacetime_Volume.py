from abc import ABC

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
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P10_falls_within(StructuredRelCl):
    pass


class E92_Spacetime_Volume(E1_CRM_Entity):
    falls_within = RelationshipFrom(
        "E92_Spacetime_Volume",
        "P10_falls_within",
        cardinality=One,
        model=P10_falls_within,
    )
