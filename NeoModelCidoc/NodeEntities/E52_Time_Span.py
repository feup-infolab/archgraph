from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, DateTimeProperty, RelationshipFrom)
from NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity
from NodeProperties.StructuredRelCl import StructuredRelCl


class P4_has_time_span(StructuredRelCl):
    pass


class E52_Time_Span(E1_CRM_Entity):
    date = DateTimeProperty(unique_index=True, required=True)
    hasTimeSpan = RelationshipFrom(E2_Temporal_Entity, 'P4_has_time_span', model=P4_has_time_span)
