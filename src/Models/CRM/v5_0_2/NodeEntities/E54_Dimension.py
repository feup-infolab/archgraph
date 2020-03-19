from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P191_had_duration import P191_had_duration
from src.Models.CRM.v5_0_2.NodeProperties.P40_observed_dimension import P40_observed_dimension
from src.Models.CRM.v5_0_2.NodeProperties.P43_has_dimension import P43_has_dimension


class E54_Dimension(E1_CRM_Entity):
    observed_dimension = RelationshipFrom(
        ".E16_Measurement.E16_Measurement",
        "P40_observed_dimension",
        model=P40_observed_dimension
    )
    has_dimension = RelationshipFrom(
        ".E70_Thing.E70_Thing",
        "P43_has_dimension",
        model=P43_has_dimension
    )
    had_duration = RelationshipFrom(
        ".E52_Time_Span.E52_Time_Span",
        "P191_had_duration",
        model=P191_had_duration
    )
