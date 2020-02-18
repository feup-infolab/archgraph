from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    StructuredRel,
)
from src.Models.CRM.NodeEntities.E24_Physical_Man_Made_Thing import E24_Physical_Man_Made_Thing
from src.Models.CRM.NodeEntities.E26_Physical_Feature import E26_Physical_Feature


class E25_Human_Made_Feature(E24_Physical_Man_Made_Thing, E26_Physical_Feature):
    pass
