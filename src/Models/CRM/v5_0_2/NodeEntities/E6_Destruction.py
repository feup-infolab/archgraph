from marshmallow import fields
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import E64_End_of_Existence, E64_End_of_ExistenceSchema
from src.Models.CRM.v5_0_2.NodeProperties.P13_destroyed import P13_destroyed


class E6_DestructionSchema(E64_End_of_ExistenceSchema):
    destroyed = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema")
    )


class E6_Destruction(E64_End_of_Existence):
    destroyed = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing", "P13_destroyed", model=P13_destroyed
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E6_DestructionSchema()

        super().__init__(schema, *args, **kwargs)
