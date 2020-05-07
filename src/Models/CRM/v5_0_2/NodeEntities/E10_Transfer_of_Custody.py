from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity, E7_ActivitySchema
from src.Models.CRM.v5_0_2.NodeProperties.P28_custody_surrenedered_by import (
    P28_custody_surrendered_by,
)
from src.Models.CRM.v5_0_2.NodeProperties.P29_custody_received_by import (
    P29_custody_received_by,
)
from src.Models.CRM.v5_0_2.NodeProperties.P30_transferred_custody_of import (
    P30_transferred_custody_of,
)


@decorator_schema
class E10_Transfer_of_CustodySchema(E7_ActivitySchema):
    custody_surrendered_by = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema")
    )
    transferred_custody_of = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema")
    )
    custody_received_by = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )


class E10_Transfer_of_Custody(E7_Activity):
    custody_surrendered_by = RelationshipTo(
        ".E53_Place.E53_Place",
        "P28_custody_surrendered_by",
        model=P28_custody_surrendered_by,
    )
    transferred_custody_of = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P30_transferred_custody_of",
        model=P30_transferred_custody_of,
    )
    custody_received_by = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P29_custody_received_by",
        model=P29_custody_received_by,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E10_Transfer_of_CustodySchema()

        super().__init__(schema, *args, **kwargs)
