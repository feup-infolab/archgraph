from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.ArchOnto.v0_1.NodeProperties.ARP8_upper_level import ARP8_upper_level
from src.Models.ArchOnto.v0_1.NodeProperties.ARP9_lower_level import ARP9_lower_level
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema


class ARE1_Level_of_DescriptionSchema(E55_TypeSchema):
    upper_level = fields.List(
        fields.Nested(
            "src.Models.ArchOnto.v0_1.NodeEntities.ARE1_Level_of_Description.ARE1_Level_of_DescriptionSchema",
        )
    )
    lower_level = fields.List(
        fields.Nested(
            "src.Models.ArchOnto.v0_1.NodeEntities.ARE1_Level_of_Description.ARE1_Level_of_DescriptionSchema",
        )
    )


class ARE1_Level_of_Description(E55_Type):
    upper_level = RelationshipTo(
        ".ARE1_Level_of_Description.ARE1_Level_of_Description",
        "ARP8_upper_level",
        model=ARP8_upper_level,
    )
    lower_level = RelationshipTo(
        ".ARE1_Level_of_Description.ARE1_Level_of_Description",
        "ARP9_lower_level",
        model=ARP9_lower_level,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE1_Level_of_DescriptionSchema()

        super().__init__(schema, *args, **kwargs)
