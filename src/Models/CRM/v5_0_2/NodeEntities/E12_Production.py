from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import E11_Modification, E11_ModificationSchema
from src.Models.CRM.v5_0_2.NodeProperties.P186_produced_thing_of_product_type import (
    P186_produced_thing_of_product_type,
)


class E12_ProductionSchema(E11_ModificationSchema):
    produced_thing_of_product_type = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E99_Product_Type.E99_Product_TypeSchema")
    )


class E12_Production(E11_Modification):
    produced_thing_of_product_type = RelationshipTo(
        ".E99_Product_Type.E99_Product_Type",
        "P186_produced_thing_of_product_type",
        model=P186_produced_thing_of_product_type,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E12_ProductionSchema()

        super().__init__(schema, *args, **kwargs)
