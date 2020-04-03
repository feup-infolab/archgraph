from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P147_curated import P147_curated


class E87_Curation_Activity(E7_Activity):
    curated = RelationshipTo(
        ".E78_Curated_Holding.E78_Curated_Holding", "P147_curated", model=P147_curated,
    )
