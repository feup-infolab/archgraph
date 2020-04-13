from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension import E54_Dimension
from src.Models.CRM.v5_0_2.NodeProperties.P179_had_sales_prices import (
    P179_had_sales_price,
)
from src.Models.CRM.v5_0_2.NodeProperties.P180_has_currency import P180_has_currency


class E97_Monetary_Amount(E54_Dimension):

    has_currency = RelationshipTo(
        ".E98_Currency.E98_Currency", "P180_has_currency", model=P180_has_currency,
    )
