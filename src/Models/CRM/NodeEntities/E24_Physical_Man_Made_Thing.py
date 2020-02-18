from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    StructuredRel,
)
from src.Models.CRM.NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from src.Models.CRM.NodeEntities.E71_Man_Made_Thing import E71_Man_Made_Thing


class E24_Physical_Man_Made_Thing(E18_Physical_Thing, E71_Man_Made_Thing):
    pass
