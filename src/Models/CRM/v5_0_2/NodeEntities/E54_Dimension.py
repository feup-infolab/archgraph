from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P40_observed_dimension import \
    P40_observed_dimension
from src.Models.CRM.v5_0_2.NodeProperties.P91_has_unit import P91_has_unit


class E54_Dimension(E1_CRM_Entity):
    has_unit = RelationshipTo(
        ".E58_Measurement_Unit.E58_Measurement_Unit", "P91_has_unit", model=P91_has_unit
    )
