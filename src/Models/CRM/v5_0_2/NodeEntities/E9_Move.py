from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity, E7_ActivitySchema
from src.Models.CRM.v5_0_2.NodeProperties.P25_moved import P25_moved
from src.Models.CRM.v5_0_2.NodeProperties.P26_moved_to import P26_moved_to
from src.Models.CRM.v5_0_2.NodeProperties.P27_moved_from import P27_moved_from


@decorator_schema
class E9_MoveSchema(E7_ActivitySchema):
    moved_to = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema")
    )
    moved_from = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema")
    )
    moved = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object.E19_Physical_ObjectSchema")
    )


class E9_Move(E7_Activity):
    moved_to = RelationshipTo(
        ".E53_Place.E53_Place", "P26_moved_to", model=P26_moved_to
    )
    moved_from = RelationshipTo(
        ".E53_Place.E53_Place", "P27_moved_from", model=P27_moved_from
    )
    moved = RelationshipTo(
        ".E19_Physical_Object.E19_Physical_Object", "P25_moved", model=P25_moved
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E9_MoveSchema()

        super().__init__(schema, *args, **kwargs)
