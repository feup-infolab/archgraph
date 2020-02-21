from abc import ABC

from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
)
from src.Models.CRM.v5_0_2.NodeEntities.E71_Man_Made_Thing import E71_Man_Made_Thing


class E28_Conceptual_Object(E71_Man_Made_Thing):
    pass
