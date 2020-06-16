from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import (
    E7_Activity,
    E7_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P143_joined import P143_joined
from src.Models.CRM.v5_0_2.NodeProperties.P144_joined_with import P144_joined_with
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E85_JoiningSchema(E7_ActivitySchema):
    joined = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    joined_with = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E74_Group.E74_GroupSchema")
    )


class E85_Joining(E7_Activity):
    joined = RelationshipTo(".E39_Actor.E39_Actor", "P143_joined", model=P143_joined)
    joined_with = RelationshipTo(
        ".E74_Group.E74_Group", "P144_joined_with", model=P144_joined_with
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E85_JoiningSchema()

        super().__init__(schema, *args, **kwargs)
