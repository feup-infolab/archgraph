from neomodel import One, RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P10_falls_within import P10_falls_within


class E92_Spacetime_Volume(E1_CRM_Entity):
    falls_within = RelationshipFrom(
        "E92_Spacetime_Volume",
        "P10_falls_within",
        cardinality=One,
        model=P10_falls_within)
