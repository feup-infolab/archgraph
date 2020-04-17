from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension import E54_Dimension, E54_DimensionSchema
from src.Models.CRM.v5_0_2.NodeProperties.P180_has_currency import P180_has_currency


class E97_Monetary_AmountSchema(E54_DimensionSchema):
    has_currency = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E98_Currency.E98_CurrencySchema")
    )


class E97_Monetary_Amount(E54_Dimension):
    has_currency = RelationshipTo(
        ".E98_Currency.E98_Currency", "P180_has_currency", model=P180_has_currency,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E97_Monetary_AmountSchema()

        super().__init__(schema, *args, **kwargs)
