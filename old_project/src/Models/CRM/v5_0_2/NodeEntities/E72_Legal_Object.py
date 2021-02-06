from marshmallow import fields, Schema
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing, E70_ThingSchema
from src.Models.CRM.v5_0_2.NodeProperties.P104_is_subject_to import P104_is_subject_to
from src.Models.CRM.v5_0_2.NodeProperties.P105_right_held_by import P105_right_held_by
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E72_Legal_ObjectSchema(E70_ThingSchema):
    P104_is_subject_to = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E30_Right.E30_RightSchema")
    )
    P105_right_held_by = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )


class E72_Legal_Object(E70_Thing):
    P104_is_subject_to = RelationshipTo(
        ".E30_Right.E30_Right", "P104_is_subject_to", model=P104_is_subject_to,
    )
    P105_right_held_by = RelationshipTo(
        ".E39_Actor.E39_Actor", "P105_right_held_by", model=P105_right_held_by,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E72_Legal_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
