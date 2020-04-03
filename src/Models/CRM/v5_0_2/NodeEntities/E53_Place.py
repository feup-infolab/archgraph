from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E4_Period import E4_Period
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import \
    E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeProperties.P7_took_place_at import \
    P7_took_place_at
from src.Models.CRM.v5_0_2.NodeProperties.P26_moved_to import P26_moved_to
from src.Models.CRM.v5_0_2.NodeProperties.P27_moved_from import P27_moved_from
from src.Models.CRM.v5_0_2.NodeProperties.P28_custody_surrenedered_by import \
    P28_custody_surrendered_by
from src.Models.CRM.v5_0_2.NodeProperties.P53_has_current_or_former_location import \
    P53_has_former_or_current_location
from src.Models.CRM.v5_0_2.NodeProperties.P54_has_current_permanent_location import \
    P54_has_current_permanent_location
from src.Models.CRM.v5_0_2.NodeProperties.P55_has_current_location import \
    P55_has_current_location
from src.Models.CRM.v5_0_2.NodeProperties.P59_has_section import \
    P59_has_section
from src.Models.CRM.v5_0_2.NodeProperties.P74_has_current_or_former_residence import \
    P74_has_current_or_former_residence
from src.Models.CRM.v5_0_2.NodeProperties.P89_falls_within import \
    P89_falls_within
from src.Models.CRM.v5_0_2.NodeProperties.P121_overlaps_with import \
    P121_overlaps_with
from src.Models.CRM.v5_0_2.NodeProperties.P122_borders_with import \
    P122_borders_with
from src.Models.CRM.v5_0_2.NodeProperties.P156_occupies import P156_occupies
from src.Models.CRM.v5_0_2.NodeProperties.P161_has_spatial_projection import \
    P161_has_spatial_projection
from src.Models.CRM.v5_0_2.NodeProperties.P189_approximates import \
    P189_approximates


class E53_Place(E1_CRM_Entity):
    occupies = RelationshipFrom(E18_Physical_Thing, "P156_occupies", model=P156_occupies)
    took_place_at = RelationshipFrom(
        E4_Period, "P7_took_place_at", model=P7_took_place_at
    )
    moved_to = RelationshipFrom(".E9_Move.E9_Move", "P26_moved_to", model=P26_moved_to)
    moved_from = RelationshipFrom(
        ".E9_Move.E9_Move", "P27_moved_from", model=P27_moved_from
    )
    custody_surrendered_by = RelationshipFrom(
        ".E10_Transfer_of_Custody.E10_Transfer_of_Custody",
        "P28_custody_surrendered_by",
        model=P28_custody_surrendered_by,
    )
    has_former_or_current_location = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P53_has_former_or_current_location",
        model=P53_has_former_or_current_location,
    )
    has_current_permanent_location = RelationshipFrom(
        ".E19_Physical_Object.E19_Physical_Object",
        "P54_has_current_permanent_location",
        model=P54_has_current_permanent_location,
    )
    has_current_location = RelationshipFrom(
        ".E19_Physical_Object.E19_Physical_Object",
        "P55_has_current_location",
        model=P55_has_current_location,
    )
    has_section = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P59_has_section",
        model=P59_has_section,
    )
    has_current_or_former_residence = RelationshipFrom(
        ".E39_Actor.E39_Actor",
        "P74_has_current_or_former_residence",
        model=P74_has_current_or_former_residence,
    )
    falls_within = RelationshipFrom(
        ".E53_Place.E53_Place", "P89_falls_within", model=P89_falls_within
    )
    overlaps_with = RelationshipFrom(
        ".E53_Place.E53_Place", "P121_overlaps_with", model=P121_overlaps_with
    )
    borders_with = RelationshipFrom(
        ".E53_Place.E53_Place", "P122_borders_with", model=P122_borders_with
    )
    has_spatial_projection = RelationshipFrom(
        ".E92_Spacetime_Volume.E92_Spacetime_Volume",
        "P161_has_spatial_projection",
        model=P161_has_spatial_projection,
    )
    approximates = RelationshipFrom(
        ".E53_Place.E53_Place", "P189_approximates", model=P189_approximates
    )
