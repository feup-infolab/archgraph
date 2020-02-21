from neomodel import One, RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity


class P10_falls_within(StructuredRel):
    pass


class E92_Spacetime_Volume(E1_CRM_Entity):
    falls_within = RelationshipFrom(
        "E92_Spacetime_Volume",
        "P10_falls_within",
        cardinality=One,
        model=P10_falls_within,
    )
