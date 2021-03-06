from marshmallow import fields
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import (
    E73_Information_Object,
    E73_Information_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P65_shows_visual_item import (
    P65_shows_visual_item,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E36_Visual_ItemSchema(E73_Information_ObjectSchema):
    P65_shows_visual_item = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_ThingSchema"
        )
    )


class E36_Visual_Item(E73_Information_Object):

    P65_shows_visual_item = RelationshipTo(
        ".E24_Physical_Human_Made_Thing.E24_Physical_Human_Made_Thing",
        "P65_shows_visual_item",
        model=P65_shows_visual_item,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E36_Visual_ItemSchema()

        super().__init__(schema, *args, **kwargs)
