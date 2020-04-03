from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import \
    E13_Attribute_Assignment
from src.Models.CRM.v5_0_2.NodeProperties.P39_measured import P39_measured
from src.Models.CRM.v5_0_2.NodeProperties.P40_observed_dimension import \
    P40_observed_dimension


class E16_Measurement(E13_Attribute_Assignment):
    measured = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P39_measured", model=P39_measured
    )
    observed_dimension = RelationshipTo(
        ".E54_Dimension.E54_Dimension",
        "P40_observed_dimension",
        model=P40_observed_dimension,
    )
