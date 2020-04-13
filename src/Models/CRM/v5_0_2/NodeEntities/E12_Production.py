from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import E11_Modification
from src.Models.CRM.v5_0_2.NodeProperties.P108_was_produced_by import (
    P108_was_produced_by,
)
from src.Models.CRM.v5_0_2.NodeProperties.P186_produced_thing_of_product_type import (
    P186_produced_thing_of_product_type,
)


class E12_Production(E11_Modification):
    produced_thing_of_product_type = RelationshipTo(
        ".E99_Product_Type.E99_Product_Type",
        "P186_produced_thing_of_product_type",
        model=P186_produced_thing_of_product_type,
    )
