from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import \
    E2_Temporal_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P7_took_place_at import \
    P7_took_place_at
from src.Models.CRM.v5_0_2.NodeProperties.P9_consists_of import P9_consists_of


class E4_Period(E2_Temporal_Entity):
    consists_of = RelationshipTo(
        ".E4_Period.E4_Period", "P9_consists_of", model=P9_consists_of
    )
    took_place_at = RelationshipTo(
        ".E53_Place.E53_Place", "P7_took_place_at", model=P7_took_place_at
    )
