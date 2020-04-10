from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P22_transferred_title_to import (
    P22_transferred_title_to,
)
from src.Models.CRM.v5_0_2.NodeProperties.P23_transferred_title_from import (
    P23_transferred_title_from,
)
from src.Models.CRM.v5_0_2.NodeProperties.P24_transferred_title_of import (
    P24_transferred_title_of,
)


class E8_Acquisition(E7_Activity):
    transferred_title_of = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P24_transferred_title_of",
        model=P24_transferred_title_of,
    )
    transferred_title_to = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P22_transferred_title_to",
        model=P22_transferred_title_to,
    )
    transferred_title_from = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P23_transferred_title_from",
        model=P23_transferred_title_from,
    )
