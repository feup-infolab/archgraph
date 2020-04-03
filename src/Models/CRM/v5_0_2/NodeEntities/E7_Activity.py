from neomodel import RelationshipTo

from ..NodeEntities.E5_Event import E5_Event
from ..NodeProperties.P14_carried_out_by import P14_carried_out_by
from ..NodeProperties.P15_was_influenced_by import P15_was_influenced_by
from ..NodeProperties.P16_used_specific_object import P16_used_specific_object
from ..NodeProperties.P17_was_motivated_by import P17_was_motivated_by
from ..NodeProperties.P19_was_intended_use_of import P19_was_intended_use_of
from ..NodeProperties.P20_had_specific_purpose import P20_had_specific_purpose
from ..NodeProperties.P21_had_general_purpose import P21_had_general_purpose
from ..NodeProperties.P32_used_general_technique import \
    P32_used_general_technique
from ..NodeProperties.P33_used_specific_technique import \
    P33_used_specific_technique
from ..NodeProperties.P125_used_object_of_type import P125_used_object_of_type
from ..NodeProperties.P134_continued import P134_continued


class E7_Activity(E5_Event):
    continued = RelationshipTo(
        ".E7_Activity.E7_Activity", "P134_continued", model=P134_continued
    )
    was_influenced_by = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P15_was_influenced_by",
        model=P15_was_influenced_by,
    )
    was_motivated_by = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P17_was_motivated_by",
        model=P17_was_motivated_by,
    )
    was_intended_use_of = RelationshipTo(
        ".E71_Human_Made_Thing.E71_Human_Made_Thing",
        "P19_was_intended_use_of",
        model=P19_was_intended_use_of,
    )
    had_general_purpose = RelationshipTo(
        ".E55_Type.E55_Type", "P21_had_general_purpose", model=P21_had_general_purpose,
    )
    used_general_technique = RelationshipTo(
        ".E55_Type.E55_Type",
        "P32_used_general_technique",
        model=P32_used_general_technique,
    )
    used_specific_object = RelationshipTo(
        ".E70_Thing.E70_Thing",
        "P16_used_specific_object",
        model=P16_used_specific_object,
    )
    used_object_of_type = RelationshipTo(
        ".E55_Type.E55_Type",
        "P125_used_object_of_type",
        model=P125_used_object_of_type,
    )
    had_specific_purpose = RelationshipTo(
        ".E5_Event.E5_Event",
        "P20_had_specific_purpose",
        model=P20_had_specific_purpose,
    )
    used_specific_technique = RelationshipTo(
        ".E29_Design_or_Procedure.E29_Design_or_Procedure",
        "P33_used_specific_technique",
        model=P33_used_specific_technique,
    )
    carried_out_by = RelationshipTo(
        ".E39_Actor.E39_Actor", "P14_carried_out_by", model=P14_carried_out_by
    )
