from neomodel import DateTimeProperty, One, RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P4_has_time_span import P4_has_time_span
from src.Models.CRM.v5_0_2.NodeProperties.P86_falls_within import P86_falls_within


class E52_Time_Span(E1_CRM_Entity):
    date = DateTimeProperty(unique_index=True, required=True)
    has_time_span = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P4_has_time_span",
        cardinality=One,
        model=P4_has_time_span)
    falls_within = RelationshipFrom(
        ".E52_Time_Span.E52_Time_Span",
        "P86_falls_within",
        model=P86_falls_within)
