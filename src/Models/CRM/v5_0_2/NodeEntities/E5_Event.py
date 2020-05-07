from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period, E4_PeriodSchema
from src.Models.CRM.v5_0_2.NodeProperties.P11_had_participat import P11_had_participant
from src.Models.CRM.v5_0_2.NodeProperties.P12_occurred_in_the_presence_of import (
    P12_occurred_in_the_presence_of,
)

@decorator_schema
class E5_EventSchema(E4_PeriodSchema):
    had_participant = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    occurred_in_the_presence_of = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item.E77_Persistent_ItemSchema")
    )
    pass


class E5_Event(E4_Period):
    had_participant = RelationshipTo(
        ".E39_Actor.E39_Actor", "P11_had_participant", model=P11_had_participant
    )
    occurred_in_the_presence_of = RelationshipTo(
        ".E77_Persistent_Item.E77_Persistent_Item",
        "P12_occurred_in_the_presence_of",
        model=P12_occurred_in_the_presence_of,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E5_EventSchema()

        super().__init__(schema, *args, **kwargs)
