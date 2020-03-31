from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeProperties.P186_produced_thing_of_product_type import \
    P186_produced_thing_of_product_type


class E99_Product_Type(E55_Type):
    produced_thing_of_product_type = RelationshipFrom(
        ".E12_Production.E12_Production",
        "P186_produced_thing_of_product_type",
        model=P186_produced_thing_of_product_type,
    )
