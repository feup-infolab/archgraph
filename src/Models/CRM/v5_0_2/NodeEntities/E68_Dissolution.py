from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import E64_End_of_Existence, E64_End_of_ExistenceSchema
from src.Models.CRM.v5_0_2.NodeProperties.P99_dissolved import P99_dissolved


class E68_DissolutionSchema(E64_End_of_ExistenceSchema):
    dissolved = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E74_Group.E74_GroupSchema")
    )


class E68_Dissolution(E64_End_of_Existence):
    dissolved = RelationshipTo(
        ".E74_Group.E74_Group", "P99_dissolved", model=P99_dissolved
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E68_DissolutionSchema()

        super().__init__(schema, *args, **kwargs)
