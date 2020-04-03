from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeProperties.P28_custody_surrenedered_by import \
    P28_custody_surrendered_by
from src.Models.CRM.v5_0_2.NodeProperties.P53_has_current_or_former_location import \
    P53_has_former_or_current_location
from src.Models.CRM.v5_0_2.NodeProperties.P54_has_current_permanent_location import \
    P54_has_current_permanent_location
from src.Models.CRM.v5_0_2.NodeProperties.P55_has_current_location import \
    P55_has_current_location
from src.Models.CRM.v5_0_2.NodeProperties.P74_has_current_or_former_residence import \
    P74_has_current_or_former_residence
from src.Models.CRM.v5_0_2.NodeProperties.P89_falls_within import \
    P89_falls_within
from src.Models.CRM.v5_0_2.NodeProperties.P121_overlaps_with import \
    P121_overlaps_with
from src.Models.CRM.v5_0_2.NodeProperties.P122_borders_with import \
    P122_borders_with
from src.Models.CRM.v5_0_2.NodeProperties.P157_is_at_rest_relative_to import \
    P157_is_at_rest_relative_to
from src.Models.CRM.v5_0_2.NodeProperties.P161_has_spatial_projection import \
    P161_has_spatial_projection
from src.Models.CRM.v5_0_2.NodeProperties.P189_approximates import \
    P189_approximates


class E53_Place(E1_CRM_Entity):
    falls_within = RelationshipTo(
        ".E53_Place.E53_Place", "P89_falls_within", model=P89_falls_within
    )
    overlaps_with = RelationshipTo(
        ".E53_Place.E53_Place", "P121_overlaps_with", model=P121_overlaps_with
    )
    borders_with = RelationshipTo(
        ".E53_Place.E53_Place", "P122_borders_with", model=P122_borders_with
    )
    approximates = RelationshipTo(
        ".E53_Place.E53_Place", "P189_approximates", model=P189_approximates
    )
    is_at_rest_relative_to = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P157_is_at_rest_relative_to",
        model=P157_is_at_rest_relative_to,
    )
