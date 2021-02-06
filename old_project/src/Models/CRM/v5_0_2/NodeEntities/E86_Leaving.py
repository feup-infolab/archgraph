from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import (
    E7_Activity,
    E7_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P145_separated import P145_separated
from src.Models.CRM.v5_0_2.NodeProperties.P146_separated_from import P146_separated_from
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E86_LeavingSchema(E7_ActivitySchema):
    separated = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    separated_from = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E74_Group.E74_GroupSchema")
    )


class E86_Leaving(E7_Activity):
    separated = RelationshipTo(
        ".E39_Actor.E39_Actor", "P145_separated_from", model=P145_separated
    )
    separated_from = RelationshipTo(
        ".E74_Group.E74_Group", "P146_separated_from", model=P146_separated_from
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E86_LeavingSchema()

        super().__init__(schema, *args, **kwargs)
