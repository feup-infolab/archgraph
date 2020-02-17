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
from NodeEntities.E90_Symbolic_Object import E90_Symbolic_Object

from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P1_is_identified_by(StructuredRelCl):
    pass


class E41_Appellation(E90_Symbolic_Object):
    is_identified_by = RelationshipFrom(
        "E1_CRM_Entity",
        "P1_is_identified_by",
        cardinality=One,
        model=P1_is_identified_by,
    )
