from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity, E2_Temporal_EntitySchema
from src.Models.CRM.v5_0_2.NodeProperties.P7_took_place_at import P7_took_place_at
from src.Models.CRM.v5_0_2.NodeProperties.P9_consists_of import P9_consists_of


class E4_PeriodSchema(E2_Temporal_EntitySchema):
    consists_of = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E4_Period.E4_PeriodSchema")
    )
    took_place_at = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema")
    )


class E4_Period(E2_Temporal_Entity):
    consists_of = RelationshipTo(
        ".E4_Period.E4_Period", "P9_consists_of", model=P9_consists_of
    )
    took_place_at = RelationshipTo(
        ".E53_Place.E53_Place", "P7_took_place_at", model=P7_took_place_at
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E4_PeriodSchema()

        super().__init__(schema, *args, **kwargs)
