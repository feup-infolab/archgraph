from marshmallow import Schema, fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import (
    E72_Legal_Object,
    E72_Legal_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P44_has_condition import P44_has_condition
from src.Models.CRM.v5_0_2.NodeProperties.P45_consists_of import P45_consists_of
from src.Models.CRM.v5_0_2.NodeProperties.P46_is_composed_of import P46_is_composed_of
from src.Models.CRM.v5_0_2.NodeProperties.P49_has_former_or_current_keeper import (
    P49_has_former_or_current_keeper,
)
from src.Models.CRM.v5_0_2.NodeProperties.P50_has_current_keeper import (
    P50_has_current_keeper,
)
from src.Models.CRM.v5_0_2.NodeProperties.P51_has_former_or_current_owner import (
    P51_has_former_or_current_owner,
)
from src.Models.CRM.v5_0_2.NodeProperties.P52_has_current_owner import (
    P52_has_current_owner,
)
from src.Models.CRM.v5_0_2.NodeProperties.P53_has_current_or_former_location import (
    P53_has_former_or_current_location,
)
from src.Models.CRM.v5_0_2.NodeProperties.P59_has_section import P59_has_section
from src.Models.CRM.v5_0_2.NodeProperties.P128_carries import P128_carries
from src.Models.CRM.v5_0_2.NodeProperties.P156_occupies import P156_occupies


@decorator_schema
class E18_Physical_ThingSchema(E72_Legal_ObjectSchema):
    P44_has_condition = fields.List(fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E3_Condition_State.E3_Condition_StateSchema")
    )
    P45_consists_of = fields.List(fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E57_Material.E57_MaterialSchema")
    )
    P46_is_composed_of = fields.List(fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema")
    )
    P49_has_former_or_current_keeper = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    P50_has_current_keeper = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    P51_has_former_or_current_owner = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    P52_has_current_owner = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E39_Actor.E39_ActorSchema")
    )
    P53_has_former_or_current_location = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema",
                      exclude=("P157_is_at_rest_relative_to",),)
    )
    P59_has_section = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema",
                      exclude=("P157_is_at_rest_relative_to",),)
    )
    P128_carries = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object.E90_Symbolic_ObjectSchema")
    )
    P156_occupies = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E53_Place.E53_PlaceSchema",
                      exclude=("P157_is_at_rest_relative_to",),)
    )


class E18_Physical_Thing(E72_Legal_Object):
    P44_has_condition = RelationshipTo(
        ".E3_Condition_State.E3_Condition_State",
        "P44_has_condition",
        model=P44_has_condition,
    )
    P45_consists_of = RelationshipTo(
        ".E57_Material.E57_Material", "P45_consists_of", model=P45_consists_of,
    )
    P46_is_composed_of = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P46_is_composed_of",
        model=P46_is_composed_of,
    )
    # took_place_on_or_within = RelationshipFrom(
    #     ".E4_Period.E4_Period",
    P49_has_former_or_current_keeper = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P49_has_former_or_current_keeper",
        model=P49_has_former_or_current_keeper,
    )
    P50_has_current_keeper = RelationshipTo(
        ".E39_Actor.E39_Actor", "P50_has_current_keeper", model=P50_has_current_keeper,
    )
    P51_has_former_or_current_owner = RelationshipTo(
        ".E39_Actor.E39_Actor",
        "P51_has_former_or_current_owner",
        model=P51_has_former_or_current_owner,
    )
    P52_has_current_owner = RelationshipTo(
        ".E39_Actor.E39_Actor", "P52_has_current_owner", model=P52_has_current_owner,
    )
    #     "P8_took_place_on_or_within",
    #     model=P8_took_place_on_or_within)
    P53_has_former_or_current_location = RelationshipTo(
        ".E53_Place.E53_Place",
        "P53_has_former_or_current_location",
        model=P53_has_former_or_current_location,
    )
    P59_has_section = RelationshipTo(
        ".E53_Place.E53_Place", "P59_has_section", model=P59_has_section,
    )
    P128_carries = RelationshipTo(
        ".E90_Symbolic_Object.E90_Symbolic_Object", "P128_carries", model=P128_carries
    )
    P156_occupies = RelationshipTo(
        ".E53_Place.E53_Place", "P156_occupies", model=P156_occupies
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E18_Physical_ThingSchema()

        super().__init__(schema, *args, **kwargs)
