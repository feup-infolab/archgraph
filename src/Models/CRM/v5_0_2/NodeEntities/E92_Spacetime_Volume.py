from marshmallow import fields
from neomodel import One, RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity, E1_CRM_EntitySchema
from src.Models.CRM.v5_0_2.NodeProperties.P10_falls_within import P10_falls_within
from src.Models.CRM.v5_0_2.NodeProperties.P132_spatiotemporally_overlaps_with import (
    P132_spatiotemporally_overlaps_with,
)
from src.Models.CRM.v5_0_2.NodeProperties.P133_is_spatiotemporally_separated_from import (
    P133_spatiotemporally_separated_from,
)
from src.Models.CRM.v5_0_2.NodeProperties.P160_has_temporal_projection import (
    P160_has_temporal_projection,
)
from src.Models.CRM.v5_0_2.NodeProperties.P161_has_spatial_projection import (
    P161_has_spatial_projection,
)


class E92_Spacetime_VolumeSchema(E1_CRM_EntitySchema):
    falls_within = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E92_Spacetime_Volume.E92_Spacetime_VolumeSchema")
    )
    spatiotemporally_overlaps_with = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E92_Spacetime_Volume.E92_Spacetime_VolumeSchema")
    )
    spatiotemporally_separated_from = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E92_Spacetime_Volume.E92_Spacetime_VolumeSchema")
    )
    has_temporal_projection = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema")
    )
    has_spatial_projection = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema")
    )


class E92_Spacetime_Volume(E1_CRM_Entity):
    falls_within = RelationshipTo(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P10_falls_within",
        cardinality=One,
        model=P10_falls_within,
    )
    spatiotemporally_overlaps_with = RelationshipTo(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P132_spatiotemporally_overlaps_with",
        model=P132_spatiotemporally_overlaps_with,
    )
    spatiotemporally_separated_from = RelationshipTo(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P133_spatiotemporally_separated_from",
        model=P133_spatiotemporally_separated_from,
    )
    has_temporal_projection = RelationshipTo(
        ".E52_Time_Span.E52_Time_Span",
        "P160_has_temporal_projection",
        model=P160_has_temporal_projection,
    )
    has_spatial_projection = RelationshipTo(
        ".E53_Place.E53_Place",
        "P161_has_spatial_projection",
        model=P161_has_spatial_projection,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E92_Spacetime_VolumeSchema()

        super().__init__(schema, *args, **kwargs)
