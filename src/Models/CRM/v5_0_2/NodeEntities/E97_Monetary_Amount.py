from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension import E54_Dimension
from src.Models.CRM.v5_0_2.NodeProperties.P179_had_sales_prices import \
    P179_had_sales_price


class E97_Monetary_Amount(E54_Dimension):
    had_sales_price = RelationshipFrom(
        ".E95_Purchase.E95_Purchase", "P179_had_sales_price", model=P179_had_sales_price
    )
