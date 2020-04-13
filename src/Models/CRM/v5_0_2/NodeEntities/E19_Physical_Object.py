from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import E18_Physical_Thing, E18_Physical_ThingSchema
from src.Models.CRM.v5_0_2.NodeProperties.P54_has_current_permanent_location import (
    P54_has_current_permanent_location,
)
from src.Models.CRM.v5_0_2.NodeProperties.P55_has_current_location import (
    P55_has_current_location,
)
from src.Models.CRM.v5_0_2.NodeProperties.P56_bears_feature import P56_bears_feature


class E19_Physical_ObjectSchema(E18_Physical_ThingSchema):
    has_current_permanent_location = fields.List(fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema",
        ))
    has_current_location = fields.List(fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema"
        ))
    # bears_feature = fields.List(fields.Nested(
    #         "src.Models.CRM.v5_0_2.NodeEntities.E26_Physical_Feature.E26_Physical_FeatureSchema"
    #     ))


class E19_Physical_Object(E18_Physical_Thing):
    has_current_permanent_location = RelationshipTo(
        ".E53_Place.E53_Place",
        "P54_has_current_permanent_location",
        model=P54_has_current_permanent_location,
    )
    has_current_location = RelationshipTo(
        ".E53_Place.E53_Place",
        "P55_has_current_location",
        model=P55_has_current_location,
    )
    bears_feature = RelationshipTo(
        ".E26_Physical_Feature.E26_Physical_Feature",
        "P56_bears_feature",
        model=P56_bears_feature,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E19_Physical_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
