from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
)
from src.Models.CRM.NodeEntities.E72_Legal_Object import E72_Legal_Object
from src.Models.CRM.NodeEntities.E28_Conceptual_Object import E28_Conceptual_Object


class E90_Symbolic_Object(E72_Legal_Object, E28_Conceptual_Object):
    pass
