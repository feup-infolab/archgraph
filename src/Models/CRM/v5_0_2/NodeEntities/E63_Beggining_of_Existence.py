from marshmallow import fields
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E5_Event import E5_Event, E5_EventSchema
from src.Models.CRM.v5_0_2.NodeProperties.P92_brought_into_existence import (
    P92_brought_into_existence,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E63_Beggining_of_ExistenceSchema(E5_EventSchema):
    brought_into_existence = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item.E77_Persistent_ItemSchema")
    )


class E63_Beggining_of_Existence(E5_Event):
    brought_into_existence = RelationshipTo(
        ".E77_Persistent_Item.E77_Persistent_Item",
        "P92_brought_into_existence",
        model=P92_brought_into_existence,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E63_Beggining_of_ExistenceSchema()

        super().__init__(schema, *args, **kwargs)
