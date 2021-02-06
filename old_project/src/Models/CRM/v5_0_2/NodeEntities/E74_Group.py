from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor, E39_ActorSchema
from src.Models.CRM.v5_0_2.NodeProperties.P107_has_current_or_former_member import (
    P107_has_current_or_former_member,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E74_GroupSchema(E39_ActorSchema):
    has_current_or_former_member = fields.List(fields.Nested(E39_ActorSchema))


class E74_Group(E39_Actor):
    has_current_or_former_member = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P107_has_current_or_former_member",
        model=P107_has_current_or_former_member,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E74_GroupSchema()

        super().__init__(schema, *args, **kwargs)
