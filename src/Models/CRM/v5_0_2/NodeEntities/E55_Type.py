from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import (
    E28_Conceptual_Object,
)
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from neomodel import StructuredRel


class P2_has_type(StructuredRel):
    pass


class P137_exemplifies(StructuredRel):
    pass


class E55_Type(E28_Conceptual_Object):
    hasType = RelationshipFrom(E1_CRM_Entity, "P2_has_type", model=P2_has_type)
    exemplifies = RelationshipFrom(
        E1_CRM_Entity, "P137_exemplifies", model=P137_exemplifies
    )
