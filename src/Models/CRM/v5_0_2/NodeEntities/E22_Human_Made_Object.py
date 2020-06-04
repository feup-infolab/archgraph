from marshmallow import fields
from neomodel import RelationshipTo

from src.Models.ArchOnto.v0_1.NodeEntities.ARE1_Level_of_Description import (
    ARE1_Level_of_Description,
)
from src.Models.ArchOnto.v0_1.NodeProperties.ARP12_has_level_of_description import (
    ARP12_has_level_of_description,
)
from src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object import (
    E19_Physical_Object,
    E19_Physical_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import (
    E24_Physical_Human_Made_Thing,
    E24_Physical_Human_Made_ThingSchema,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E22_Human_Made_ObjectSchema(
    E19_Physical_ObjectSchema, E24_Physical_Human_Made_ThingSchema
):
    has_level_of_description = fields.List(
        fields.Nested(
            "src.Models.ArchOnto.v0_1.NodeEntities.ARE1_Level_of_Description.ARE1_Level_of_DescriptionSchema",
        )
    )


class E22_Human_Made_Object(E19_Physical_Object, E24_Physical_Human_Made_Thing):

    has_level_of_description = RelationshipTo(
        ARE1_Level_of_Description,
        "ARP12_has_level_of_description",
        model=ARP12_has_level_of_description,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E22_Human_Made_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
