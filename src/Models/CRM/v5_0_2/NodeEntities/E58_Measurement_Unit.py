from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeProperties.P91_has_unit import P91_has_unit


class E58_Measurement_Unit(E55_Type):
    has_unit = RelationshipFrom(
        ".E54_Dimension.E54_Dimension",
        "P91_has_unit",
        model=P91_has_unit)
