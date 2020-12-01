from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import (
    E7_Activity,
    E7_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P22_transferred_title_to import (
    P22_transferred_title_to,
)
from src.Models.CRM.v5_0_2.NodeProperties.P23_transferred_title_from import (
    P23_transferred_title_from,
)
from src.Models.CRM.v5_0_2.NodeProperties.P24_transferred_title_of import (
    P24_transferred_title_of,
)


@decorator_schema
class E8_AcquisitionSchema(E7_ActivitySchema):
    transferred_title_of = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema"
        )
    )
    transferred_title_to = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    transferred_title_from = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )


class E8_Acquisition(E7_Activity):
    transferred_title_of = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P24_transferred_title_of",
        model=P24_transferred_title_of,
    )
    transferred_title_to = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P22_transferred_title_to",
        model=P22_transferred_title_to,
    )
    transferred_title_from = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P23_transferred_title_from",
        model=P23_transferred_title_from,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E8_AcquisitionSchema()

        super().__init__(schema, *args, **kwargs)
