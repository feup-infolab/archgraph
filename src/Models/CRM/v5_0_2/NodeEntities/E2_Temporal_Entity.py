from marshmallow import Schema, fields
from neomodel import One, RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import (
    E1_CRM_Entity,
    E1_CRM_EntitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P4_has_time_span import P4_has_time_span
from src.Models.CRM.v5_0_2.NodeProperties.P114_is_equal_in_time_to import (
    P114_is_equal_in_time_to,
)
from src.Models.CRM.v5_0_2.NodeProperties.P115_finished import P115_finishes
from src.Models.CRM.v5_0_2.NodeProperties.P116_starts import P116_starts
from src.Models.CRM.v5_0_2.NodeProperties.P117_occurs_during import P117_occurs_during
from src.Models.CRM.v5_0_2.NodeProperties.P118_overlaps_in_time_with import (
    P118_overlaps_in_time_with,
)
from src.Models.CRM.v5_0_2.NodeProperties.P119_meets_in_time_with import (
    P119_meets_in_time_with,
)
from src.Models.CRM.v5_0_2.NodeProperties.P120_occurs_before import P120_occurs_before
from src.Models.CRM.v5_0_2.NodeProperties.P173_starts_before_or_with_the_end_of import (
    P173_starts_before_or_with_the_end_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P174_starts_before_the_end_of import (
    P174_starts_before_the_end_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P175_starts_before_or_with_the_start_of import (
    P175_starts_before_or_with_the_start_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P176_starts_before_the_start_of import (
    P176_starts_before_the_start_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P182_ends_before_or_with_the_start_of import (
    P182_ends_before_or_with_the_start_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P183_ends_before_the_start_of import (
    P183_ends_before_the_start_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P184_ends_before_or_with_the_end_of import (
    P184_ends_before_or_with_the_end_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P185_ends_before_the_end_of import (
    P185_ends_before_the_end_of,
)


class E2_Temporal_EntitySchema(E1_CRM_EntitySchema):
    P4_has_time_span = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P114_is_equal_in_time_to = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P115_finishes = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P116_starts = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P117_occurs_during = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P118_overlaps_in_time_with = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P119_meets_in_time_with = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P120_occurs_before = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P173_starts_before_or_with_the_end_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P174_starts_before_the_end_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P175_starts_before_or_with_the_start_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span" ".E52_Time_SpanSchema"
    )
    P176_starts_before_the_start_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P182_ends_before_or_with_the_start_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P183_ends_before_the_start_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )
    P184_ends_before_or_with_the_end_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span" ".E52_Time_SpanSchema"
    )
    P185_ends_before_the_end_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"
    )


class E2_Temporal_Entity(E1_CRM_Entity):
    P4_has_time_span = RelationshipTo(
        ".E52_Time_Span.E52_Time_Span",
        "P4_has_time_span",
        cardinality=One,
        model=P4_has_time_span,
    )
    P114_is_equal_in_time_to = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P114_is_equal_in_time_to",
        cardinality=One,
        model=P114_is_equal_in_time_to,
    )
    P115_finishes = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P115_finishes",
        cardinality=One,
        model=P115_finishes,
    )
    P116_starts = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P116_starts",
        cardinality=One,
        model=P116_starts,
    )
    P117_occurs_during = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P117_occurs_during",
        cardinality=One,
        model=P117_occurs_during,
    )
    P118_overlaps_in_time_with = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P118_overlaps_in_time_with",
        cardinality=One,
        model=P118_overlaps_in_time_with,
    )
    P119_meets_in_time_with = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P119_meets_in_time_with",
        cardinality=One,
        model=P119_meets_in_time_with,
    )
    P120_occurs_before = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P120_occurs_before",
        cardinality=One,
        model=P120_occurs_before,
    )
    P173_starts_before_or_with_the_end_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P173_starts_before_or_with_the_end_of",
        cardinality=One,
        model=P173_starts_before_or_with_the_end_of,
    )
    P174_starts_before_the_end_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P174_starts_before_the_end_of",
        cardinality=One,
        model=P174_starts_before_the_end_of,
    )
    P175_starts_before_or_with_the_start_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P175_starts_before_or_with_the_start_of",
        cardinality=One,
        model=P175_starts_before_or_with_the_start_of,
    )
    P176_starts_before_the_start_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P176_starts_before_the_start_of",
        cardinality=One,
        model=P176_starts_before_the_start_of,
    )
    P182_ends_before_or_with_the_start_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P182_ends_before_or_with_the_start_of",
        cardinality=One,
        model=P182_ends_before_or_with_the_start_of,
    )
    P183_ends_before_the_start_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P183_ends_before_the_start_of",
        cardinality=One,
        model=P183_ends_before_the_start_of,
    )
    P184_ends_before_or_with_the_end_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P184_ends_before_or_with_the_end_of",
        cardinality=One,
        model=P184_ends_before_or_with_the_end_of,
    )
    P185_ends_before_the_end_of = RelationshipTo(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P185_ends_before_the_end_of",
        cardinality=One,
        model=P185_ends_before_the_end_of,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E2_Temporal_EntitySchema()

        super().__init__(schema, *args, **kwargs)
