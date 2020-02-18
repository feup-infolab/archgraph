from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    DateTimeProperty,
    One,
    RelationshipFrom,
)
from src.Models.CRM.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P4_has_time_span(StructuredRelCl):
    pass


class E52_Time_Span(E1_CRM_Entity):
    date = DateTimeProperty(unique_index=True, required=True)
    has_time_span = RelationshipFrom(
        "E2_Temporal_Entity",
        "P4_has_time_span",
        cardinality=One,
        model=P4_has_time_span,
    )
