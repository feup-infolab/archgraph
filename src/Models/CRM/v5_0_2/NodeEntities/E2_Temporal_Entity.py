from neomodel import One, RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P114_is_equal_in_time_to import \
    P114_is_equal_in_time_to
from src.Models.CRM.v5_0_2.NodeProperties.P115_finished import P115_finishes
from src.Models.CRM.v5_0_2.NodeProperties.P116_starts import P116_starts
from src.Models.CRM.v5_0_2.NodeProperties.P117_occurs_during import \
    P117_occurs_during
from src.Models.CRM.v5_0_2.NodeProperties.P118_overlaps_in_time_with import \
    P118_overlaps_in_time_with
from src.Models.CRM.v5_0_2.NodeProperties.P119_meets_in_time_with import \
    P119_meets_in_time_with
from src.Models.CRM.v5_0_2.NodeProperties.P120_occurs_before import \
    P120_occurs_before
from src.Models.CRM.v5_0_2.NodeProperties.P173_starts_before_or_with_the_end_of import \
    P173_starts_before_or_with_the_end_of
from src.Models.CRM.v5_0_2.NodeProperties.P174_starts_before_the_end_of import \
    P174_starts_before_the_end_of
from src.Models.CRM.v5_0_2.NodeProperties.P175_starts_before_or_with_the_start_of import \
    P175_starts_before_or_with_the_start_of
from src.Models.CRM.v5_0_2.NodeProperties.P176_starts_before_the_start_of import \
    P176_starts_before_the_start_of
from src.Models.CRM.v5_0_2.NodeProperties.P182_ends_before_or_with_the_start_of import \
    P182_ends_before_or_with_the_start_of
from src.Models.CRM.v5_0_2.NodeProperties.P183_ends_before_the_start_of import \
    P183_ends_before_the_start_of
from src.Models.CRM.v5_0_2.NodeProperties.P184_ends_before_or_with_the_end_of import \
    P184_ends_before_or_with_the_end_of
from src.Models.CRM.v5_0_2.NodeProperties.P185_ends_before_the_end_of import \
    P185_ends_before_the_end_of


class E2_Temporal_Entity(E1_CRM_Entity):
    is_equal_in_time_to = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P114_is_equal_in_time_to",
        cardinality=One,
        model=P114_is_equal_in_time_to,
    )
    finishes = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P115_finishes",
        cardinality=One,
        model=P115_finishes,
    )
    starts = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P116_starts",
        cardinality=One,
        model=P116_starts,
    )
    occurs_during = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P117_occurs_during",
        cardinality=One,
        model=P117_occurs_during,
    )
    overlaps_in_time_with = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P118_overlaps_in_time_with",
        cardinality=One,
        model=P118_overlaps_in_time_with,
    )
    meets_in_time_with = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P119_meets_in_time_with",
        cardinality=One,
        model=P119_meets_in_time_with,
    )
    occurs_before = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P120_occurs_before",
        cardinality=One,
        model=P120_occurs_before,
    )
    starts_before_or_at_the_end_of = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P173_starts_before_or_with_the_end_of",
        cardinality=One,
        model=P173_starts_before_or_with_the_end_of,
    )
    starts_before = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P174_starts_before_the_end_of",
        cardinality=One,
        model=P174_starts_before_the_end_of,
    )
    starts_before_or_with_the_start_of = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P175_starts_before_or_with_the_start_of",
        cardinality=One,
        model=P175_starts_before_or_with_the_start_of,
    )
    starts_before_the_start_of = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P176_starts_before_the_start_of",
        cardinality=One,
        model=P176_starts_before_the_start_of,
    )
    ends_before_or_at_the_start_of = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P182_ends_before_or_with_the_start_of",
        cardinality=One,
        model=P182_ends_before_or_with_the_start_of,
    )
    ends_before_the_start_of = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P183_ends_before_the_start_of",
        cardinality=One,
        model=P183_ends_before_the_start_of,
    )
    ends_before_or_wit_the_end_of = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P184_ends_before_or_with_the_end_of",
        cardinality=One,
        model=P184_ends_before_or_with_the_end_of,
    )
    ends_before_the_end_of = RelationshipFrom(
        ".E2_Temporal_Entity.E2_Temporal_Entity",
        "P185_ends_before_the_end_of",
        cardinality=One,
        model=P185_ends_before_the_end_of,
    )
