from marshmallow import Schema, fields
from neomodel import RelationshipTo

from src.Models.CRM.v5_0_2.NodeEntities.E77_Persistent_Item import (
    E77_Persistent_Item,
    E77_Persistent_ItemSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P43_has_dimension import P43_has_dimension
from src.Models.CRM.v5_0_2.NodeProperties.P101_had_as_general_use import (
    P101_had_as_general_use,
)
from src.Models.CRM.v5_0_2.NodeProperties.P130_shows_features_of import (
    P130_shows_features_of,
)
from src.GCF.decorators.OntologyClass import decorator_schema


#todo
@decorator_schema
class E70_ThingSchema(E77_Persistent_ItemSchema):
    P130_shows_features_of = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E70_Thing.E70_ThingSchema")
    )
    #P101_had_as_general_use = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema"))
    #P43_has_dimension = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension.E54_DimensionSchema"))


class E70_Thing(E77_Persistent_Item):
    P130_shows_features_of = RelationshipTo(
        ".E70_Thing.E70_Thing", "P130_shows_features_of", model=P130_shows_features_of
    )
    P101_had_as_general_use = RelationshipTo(
        ".E55_Type.E55_Type", "P101_had_as_general_use", model=P101_had_as_general_use
    )
    P43_has_dimension = RelationshipTo(
        ".E54_Dimension.E54_Dimension", "P43_has_dimension", model=P43_has_dimension
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E70_ThingSchema()

        super().__init__(schema, *args, **kwargs)
