from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P28_custody_surrenedered_by import \
    P28_custody_surrendered_by
from src.Models.CRM.v5_0_2.NodeProperties.P29_custody_received_by import \
    P29_custody_received_by
from src.Models.CRM.v5_0_2.NodeProperties.P30_transferred_custody_of import \
    P30_transferred_custody_of


class E10_Transfer_of_Custody(E7_Activity):
    custody_surrendered_by = RelationshipTo(
        ".E53_Place.E53_Place",
        "P28_custody_surrendered_by",
        model=P28_custody_surrendered_by,
    )
    transferred_custody_of = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P30_transferred_custody_of",
        model=P30_transferred_custody_of,
    )
    custody_received_by = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P29_custody_received_by",
        model=P29_custody_received_by,
    )
