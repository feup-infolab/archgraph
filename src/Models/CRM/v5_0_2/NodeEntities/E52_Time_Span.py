from neomodel import One, RelationshipFrom, DateTimeFormatProperty
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P4_has_time_span import \
    P4_has_time_span
from src.Models.CRM.v5_0_2.NodeProperties.P86_falls_within import \
    P86_falls_within
from src.Models.CRM.v5_0_2.NodeProperties.P160_has_temporal_projection import \
    P160_has_temporal_projection
from src.Models.CRM.v5_0_2.NodeProperties.P164_during import P164_during


class E52_Time_Span(E1_CRM_Entity):
    date = DateTimeFormatProperty(
        format="%Y-%m-%d", unique_index=True, required=True
    )
    has_time_span = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P4_has_time_span",
        cardinality=One,
        model=P4_has_time_span,
    )
    falls_within = RelationshipFrom(
        ".E52_Time_Span.E52_Time_Span", "P86_falls_within", model=P86_falls_within
    )
    has_temporal_projection = RelationshipFrom(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P160_has_temporal_projection",
        model=P160_has_temporal_projection,
    )
    has_spatial_projection = RelationshipFrom(
        ".E93_Presence.E93_Presence", "P164_during", model=P164_during
    )
