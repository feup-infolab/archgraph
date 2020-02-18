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
from src.Models.CRM.NodeEntities.E8_Acquisition import E8_Acquisition


class E96_Purchase(E8_Acquisition):
    pass
