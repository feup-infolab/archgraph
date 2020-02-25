from neomodel import One, RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P10_falls_within import P10_falls_within
from src.Models.CRM.v5_0_2.NodeProperties.P132_spatiotemporally_overlaps_with import P132_spatiotemporally_overlaps_with
from src.Models.CRM.v5_0_2.NodeProperties.P133_is_spatiotemporally_separated_from import \
    P133_spatiotemporally_separated_from


class E92_Spacetime_Volume(E1_CRM_Entity):
    falls_within = RelationshipFrom(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P10_falls_within",
        cardinality=One,
        model=P10_falls_within)
    spatiotemporally_overlaps_with = RelationshipFrom(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P132_spatiotemporally_overlaps_with",
        model=P132_spatiotemporally_overlaps_with)
    spatiotemporally_separated_from = RelationshipFrom(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P133_spatiotemporally_separated_from",
        model=P133_spatiotemporally_separated_from)
