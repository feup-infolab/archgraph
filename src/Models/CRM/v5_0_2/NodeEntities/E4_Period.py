from neomodel import RelationshipFrom, StructuredRel

from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import \
    E2_Temporal_Entity


class P9_consists_of(StructuredRel):
    pass


class E4_Period(E2_Temporal_Entity):
    consists_of = RelationshipFrom("E4_Period", "P9_consists_of", model=P9_consists_of)
