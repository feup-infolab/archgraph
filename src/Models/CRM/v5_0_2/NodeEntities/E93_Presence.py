from abc import ABC

from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
)
from src.Models.CRM.v5_0_2.NodeEntities.E92_Spacetime_Volume import E92_Spacetime_Volume


class E93_Presence(E92_Spacetime_Volume):
    pass
