from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import \
    E24_Physical_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P147_curated import P147_curated


class E78_Curated_Holding(E24_Physical_Human_Made_Thing):
    curated = RelationshipFrom(
        ".E87_Curation_Activity.E87_E87_Curation_Activity",
        "P147_curated",
        model=P147_curated,
    )
