from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import (
    E11_Modification,
    E11_ModificationSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P110_augmented import P110_augmented
from src.Models.CRM.v5_0_2.NodeProperties.P111_added import P111_added
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E79_Part_AdditionSchema(E11_ModificationSchema):
    augmented = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_ThingSchema"
        )
    )
    added = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema"
        )
    )


class E79_Part_Addition(E11_Modification):
    augmented = RelationshipTo(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing",
        "P110_augmented",
        model=P110_augmented,
    )
    added = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing", "P111_added", model=P111_added
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E79_Part_AdditionSchema()

        super().__init__(schema, *args, **kwargs)
