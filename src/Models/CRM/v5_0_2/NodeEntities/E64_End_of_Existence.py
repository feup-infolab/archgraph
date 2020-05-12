from marshmallow import fields
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event, E5_EventSchema
from src.Models.CRM.v5_0_2.NodeProperties.P93_took_out_of_existence import (
    P93_took_out_of_existence,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E64_End_of_ExistenceSchema(E5_EventSchema):
    took_out_of_existence = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item.E77_Persistent_ItemSchema")
    )


class E64_End_of_Existence(E5_Event):
    took_out_of_existence = RelationshipTo(
        ".E77_Persistent_Item.E77_Persistent_Item",
        "P93_took_out_of_existence",
        model=P93_took_out_of_existence,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E64_End_of_ExistenceSchema()

        super().__init__(schema, *args, **kwargs)
