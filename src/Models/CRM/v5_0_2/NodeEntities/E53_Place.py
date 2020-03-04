from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P156_occupies import P156_occupies
from src.Models.CRM.v5_0_2.NodeProperties.P7_took_place_at import \
    P7_took_place_at


class E53_Place(E1_CRM_Entity):
    occupies = RelationshipTo(E18_Physical_Thing, "P156_occupies", model=P156_occupies)
    took_place_at = RelationshipTo(
        E18_Physical_Thing, "P7_took_place_at", model=P7_took_place_at
    )
