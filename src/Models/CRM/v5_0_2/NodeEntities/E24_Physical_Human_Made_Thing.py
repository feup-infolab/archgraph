from marshmallow import Schema, fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import (
    E18_Physical_Thing,
    E18_Physical_ThingSchema,
)
from src.Models.CRM.v5_0_2.NodeEntities.E71_Human_Made_Thing import E71_Human_Made_Thing, E71_Human_Made_ThingSchema
from src.Models.CRM.v5_0_2.NodeProperties.P62_depicts import P62_depicts
from src.Models.CRM.v5_0_2.NodeProperties.P108_was_produced_by import (
    P108_was_produced_by,
)


# TODO na linha de baixo falta fazer um import
class E24_Physical_Human_Made_ThingSchema(E71_Human_Made_ThingSchema):
    P62_depicts = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema",
            exclude=("P138_represents",)
        )
    )
    # P108_has_produced_by = fields.List(
    #     fields.Nested(
    #         "src.Models.CRM.v5_0_2.NodeEntities.E12_Production.E12_ProductionSchema",
    #         exclude=("P138_represents",)
    #     )
    # )


class E24_Physical_Human_Made_Thing(E18_Physical_Thing, E71_Human_Made_Thing):
    P62_depicts = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P62_depicts", model=P62_depicts,
    )
    P108_has_produced_by = RelationshipTo(
        ".E12_Production.E12_Production",
        "P108_has_produced_by",
        model=P108_was_produced_by,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E24_Physical_Human_Made_ThingSchema()

        super().__init__(schema, *args, **kwargs)
