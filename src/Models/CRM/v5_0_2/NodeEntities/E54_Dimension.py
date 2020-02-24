from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P40_observed_dimension import P40_observed_dimension


class E54_Dimension(E1_CRM_Entity):
    observed_dimension = RelationshipFrom(
        ".E16_Measurement.E16_Measurement",
        "P40_observed_dimension",
        model=P40_observed_dimension)
