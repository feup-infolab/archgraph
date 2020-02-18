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
from src.Models.CRM.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P114_is_equal_in_time_to(StructuredRelCl):
    pass


class P115_finishes(StructuredRelCl):
    pass


class P116_starts(StructuredRelCl):
    pass


class P117_occurs_during(StructuredRelCl):
    pass


class P118_overlaps_in_time_with(StructuredRelCl):
    pass


class P119_meets_in_time_with(StructuredRelCl):
    pass


class P120_occurs_before(StructuredRelCl):
    pass


class P173_starts_before_or_at_the_end_of(StructuredRelCl):
    pass


class P174_starts_before(StructuredRelCl):
    pass


class P175_starts_before_or_with_the_start_of(StructuredRelCl):
    pass


class P176_starts_before_the_start_of(StructuredRelCl):
    pass


class P182_ends_before_or_at_the_start_of(StructuredRelCl):
    pass


class P183_ends_before_the_start_of(StructuredRelCl):
    pass


class P184_ends_before_or_wit_the_end_of(StructuredRelCl):
    pass


class P185_ends_before_the_end_of(StructuredRelCl):
    pass


class E2_Temporal_Entity(E1_CRM_Entity):
    is_equal_in_time_to = RelationshipFrom(
        "E2_Temporal_Entity",
        "P114_is_equal_in_time_to",
        cardinality=One,
        model=P114_is_equal_in_time_to,
    )
    finishes = RelationshipFrom(
        "E2_Temporal_Entity", "P115_finishes", cardinality=One, model=P115_finishes
    )
    starts = RelationshipFrom(
        "E2_Temporal_Entity", "P116_starts", cardinality=One, model=P116_starts
    )
    occurs_during = RelationshipFrom(
        "E2_Temporal_Entity",
        "P117_occurs_during",
        cardinality=One,
        model=P117_occurs_during,
    )
    overlaps_in_time_with = RelationshipFrom(
        "E2_Temporal_Entity",
        "P118_overlaps_in_time_with",
        cardinality=One,
        model=P118_overlaps_in_time_with,
    )
    meets_in_time_with = RelationshipFrom(
        "E2_Temporal_Entity",
        "P119_meets_in_time_with",
        cardinality=One,
        model=P119_meets_in_time_with,
    )
    occurs_before = RelationshipFrom(
        "E2_Temporal_Entity",
        "P120_occurs_before",
        cardinality=One,
        model=P120_occurs_before,
    )
    starts_before_or_at_the_end_of = RelationshipFrom(
        "E2_Temporal_Entity",
        "P173_starts_before_or_at_the_end_of",
        cardinality=One,
        model=P173_starts_before_or_at_the_end_of,
    )
    starts_before = RelationshipFrom(
        "E2_Temporal_Entity",
        "P174_starts_before",
        cardinality=One,
        model=P174_starts_before,
    )
    starts_before_or_with_the_start_of = RelationshipFrom(
        "E2_Temporal_Entity",
        "P175_starts_before_or_with_the_start_of",
        cardinality=One,
        model=P175_starts_before_or_with_the_start_of,
    )
    starts_before_the_start_of = RelationshipFrom(
        "E2_Temporal_Entity",
        "P176_starts_before_the_start_of",
        cardinality=One,
        model=P176_starts_before_the_start_of,
    )
    ends_before_or_at_the_start_of = RelationshipFrom(
        "E2_Temporal_Entity",
        "P182_ends_before_or_at_the_start_of",
        cardinality=One,
        model=P182_ends_before_or_at_the_start_of,
    )
    ends_before_the_start_of = RelationshipFrom(
        "E2_Temporal_Entity",
        "P183_ends_before_the_start_of",
        cardinality=One,
        model=P183_ends_before_the_start_of,
    )
    ends_before_or_wit_the_end_of = RelationshipFrom(
        "E2_Temporal_Entity",
        "P184_ends_before_or_wit_the_end_of",
        cardinality=One,
        model=P184_ends_before_or_wit_the_end_of,
    )
    ends_before_the_end_of = RelationshipFrom(
        "E2_Temporal_Entity",
        "P185_ends_before_the_end_of",
        cardinality=One,
        model=P185_ends_before_the_end_of,
    )
