from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E11_Modification import E11_Modification, E11_ModificationSchema
from src.Models.CRM.v5_0_2.NodeProperties.P112_diminished import P112_diminished
from src.Models.CRM.v5_0_2.NodeProperties.P113_removed import P113_removed
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E80_Part_RemovalSchema(E11_ModificationSchema):
    diminished = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_ThingSchema")
    )
    removed = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema")
    )


class E80_Part_Removal(E11_Modification):
    diminished = RelationshipTo(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing",
        "P112_diminished",
        model=P112_diminished,
    )

    removed = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing", "P113_removed", model=P113_removed
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E80_Part_RemovalSchema()

        super().__init__(schema, *args, **kwargs)
