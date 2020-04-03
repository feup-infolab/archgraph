from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import \
    E24_Physical_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P109_has_current_or_former_curator import \
    P109_has_current_or_former_curator


class E78_Curated_Holding(E24_Physical_Human_Made_Thing):
    has_current_or_former_curator = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P109_has_current_or_former_curator",
        model=P109_has_current_or_former_curator,
    )
