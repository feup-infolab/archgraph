from neomodel import RelationshipTo, RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period
from src.Models.CRM.v5_0_2.NodeProperties.P26_moved_to import P26_moved_to
from src.Models.CRM.v5_0_2.NodeProperties.P27_moved_from import P27_moved_from
from src.Models.CRM.v5_0_2.NodeProperties.P28_custody_surrenedered_by import P28_custody_surrendered_by
from src.Models.CRM.v5_0_2.NodeProperties.P7_took_place_at import \
    P7_took_place_at
from src.Models.CRM.v5_0_2.NodeProperties.P156_occupies import P156_occupies




class E53_Place(E1_CRM_Entity):
    occupies = RelationshipTo(E18_Physical_Thing, "P156_occupies", model=P156_occupies)
    took_place_at = RelationshipFrom(
        E4_Period, "P7_took_place_at", model=P7_took_place_at
    )
    moved_to = RelationshipFrom(
        ".E9_Move.E9_Move",
        "P26_moved_to",
        model=P26_moved_to)
    moved_from = RelationshipFrom(
        ".E9_Move.E9_Move",
        "P27_moved_from",
        model=P27_moved_from)
    custody_surrendered_by = RelationshipFrom(
        ".E10_Transfer_of_Custody.E10_Transfer_of_Custody",
        "P28_custody_surrendered_by",
        model=P28_custody_surrendered_by
    )
