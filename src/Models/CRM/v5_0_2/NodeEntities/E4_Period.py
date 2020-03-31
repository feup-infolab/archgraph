from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import \
    E2_Temporal_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P9_consists_of import P9_consists_of


class E4_Period(E2_Temporal_Entity):
    consists_of = RelationshipFrom("E4_Period", "P9_consists_of", model=P9_consists_of)
