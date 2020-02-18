from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
)
from src.Models.CRM.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P01_has_domain(StructuredRelCl):
    pass


class P02_has_range(StructuredRelCl):
    pass


class PC0_CRM_Property(E1_CRM_Entity):
    hasDomain = RelationshipTo(
        E1_CRM_Entity, "P01_has_domain", cardinality=One, model=P01_has_domain
    )
    hasRange = RelationshipTo(
        E1_CRM_Entity, "P02_has_range", cardinality=One, model=P02_has_range
    )
