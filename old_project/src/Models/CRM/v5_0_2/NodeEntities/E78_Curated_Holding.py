from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import (
    E24_Physical_Human_Made_Thing,
    E24_Physical_Human_Made_ThingSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_ActorSchema
from src.Models.CRM.v5_0_2.NodeProperties.P109_has_current_or_former_curator import (
    P109_has_current_or_former_curator,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E78_Curated_HoldingSchema(E24_Physical_Human_Made_ThingSchema):
    has_current_or_former_curator = fields.List(fields.Nested(E39_ActorSchema))


class E78_Curated_Holding(E24_Physical_Human_Made_Thing):
    has_current_or_former_curator = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P109_has_current_or_former_curator",
        model=P109_has_current_or_former_curator,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E78_Curated_HoldingSchema()

        super().__init__(schema, *args, **kwargs)
