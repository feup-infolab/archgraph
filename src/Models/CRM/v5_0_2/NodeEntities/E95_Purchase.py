from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E8_Acquisition import E8_Acquisition, E8_AcquisitionSchema
from src.Models.CRM.v5_0_2.NodeProperties.P179_had_sales_prices import (
    P179_had_sales_price,
)


class E95_PurchaseSchema(E8_AcquisitionSchema):
    had_sales_price = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E97_Monetary_Amount.E97_Monetary_AmountSchema")
    )


class E95_Purchase(E8_Acquisition):
    had_sales_price = RelationshipTo(
        ".E97_Monetary_Amount.E97_Monetary_Amount",
        "P179_had_sales_price",
        model=P179_had_sales_price,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E95_PurchaseSchema()

        super().__init__(schema, *args, **kwargs)
