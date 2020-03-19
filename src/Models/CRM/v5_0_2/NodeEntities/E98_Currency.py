from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeEntities.E58_Measurement_Unit import \
    E58_Measurement_Unit
from src.Models.CRM.v5_0_2.NodeProperties.P180_has_currency import P180_has_currency


class E98_Currency(E55_Type, E58_Measurement_Unit):
    has_currency = RelationshipFrom(
        ".E97_Monetary_Amount.E97_Monetary_Amount",
        "P180_has_currency",
        model=P180_has_currency
    )
