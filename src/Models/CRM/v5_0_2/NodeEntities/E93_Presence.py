from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E92_Spacetime_Volume import E92_Spacetime_Volume, E92_Spacetime_VolumeSchema
from src.Models.CRM.v5_0_2.NodeProperties.P164_during import P164_during
from src.Models.CRM.v5_0_2.NodeProperties.P166_was_a_presence_of import (
    P166_was_a_presence_of,
)
from src.Models.CRM.v5_0_2.NodeProperties.P167_at import P167_at


class E93_PresenceSchema(E92_Spacetime_VolumeSchema):
    was_a_presence_of = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E92_Spacetime_Volume.E92_Spacetime_VolumeSchema")
    )
    at = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E57_Material.E57_MaterialSchema")
    )
    has_spatial_projection = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema")
    )


class E93_Presence(E92_Spacetime_Volume):
    was_a_presence_of = RelationshipTo(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P166_was_a_presence_of",
        model=P166_was_a_presence_of,
    )
    at = RelationshipTo(".E57_Material.E57_Material", "P167_at", model=P167_at)
    has_spatial_projection = RelationshipTo(
        ".E52_Time_Span.E52_Time_Span", "P164_during", model=P164_during
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E93_PresenceSchema()

        super().__init__(schema, *args, **kwargs)
