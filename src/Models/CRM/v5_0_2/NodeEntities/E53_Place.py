from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from neomodel import StructuredRel


class P156_occupies(StructuredRel):
    pass


class P7_took_place_at(StructuredRel):
    pass


class E53_Place(E1_CRM_Entity):
    occupies = RelationshipFrom(
        E18_Physical_Thing, "P156_occupies", model=P156_occupies
    )
    took_place_at = RelationshipFrom(
        E18_Physical_Thing, "P7_took_place_at", model=P7_took_place_at
    )
