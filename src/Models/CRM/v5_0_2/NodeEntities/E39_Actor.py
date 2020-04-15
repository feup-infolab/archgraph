from marshmallow import Schema, fields
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import (
    E77_Persistent_Item,
    E77_Persistent_ItemSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P74_has_current_or_former_residence import (
    P74_has_current_or_former_residence,
)
from src.Models.CRM.v5_0_2.NodeProperties.P75_possesses import P75_possesses


class E39_ActorSchema(E77_Persistent_ItemSchema):
    P74_has_current_or_former_residence = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema",
                      exclude=("P157_is_at_rest_relative_to",))
    )
    P75_possesses = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E30_Right.E30_RightSchema")
    )


class E39_Actor(E77_Persistent_Item):
    P74_has_current_or_former_residence = RelationshipTo(
        ".E53_Place.E53_Place",
        "P74_has_current_or_former_residence",
        model=P74_has_current_or_former_residence,
    )
    P75_possesses = RelationshipTo(
        ".E30_Right.E30_Right", "P75_possesses", model=P75_possesses
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E39_ActorSchema()

        super().__init__(schema, *args, **kwargs)
