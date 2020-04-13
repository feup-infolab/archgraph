from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E8_Acquisition import E8_Acquisition
from src.Models.CRM.v5_0_2.NodeProperties.P179_had_sales_prices import (
    P179_had_sales_price,
)


class E95_Purchase(E8_Acquisition):
    had_sales_price = RelationshipTo(
        ".E97_Monetary_Amount.E97_Monetary_Amount",
        "P179_had_sales_price",
        model=P179_had_sales_price,
    )
