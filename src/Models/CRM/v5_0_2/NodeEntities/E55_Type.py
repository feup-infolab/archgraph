from neomodel import RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object
from ..NodeProperties.P177_assigned_property_type import P177_assigned_property_type
from ..NodeProperties.P101_had_as_general_use import P101_had_as_general_use
from ..NodeProperties.P103_was_intended_for import P103_was_intended_for
from ..NodeProperties.P125_used_object_of_type import P125_used_object_of_type
from ..NodeProperties.P127_has_broader_term import P127_has_broader_term
from ..NodeProperties.P135_created_type import P135_created_type
from ..NodeProperties.P137_exemplifies import P137_exemplifies
from ..NodeProperties.P150_defines_typical_parts_of import P150_defines_typical_parts_of
from ..NodeProperties.P21_had_general_purpose import P21_had_general_purpose
from ..NodeProperties.P2_has_type import P2_has_type
from ..NodeProperties.P32_used_general_technique import P32_used_general_technique
from ..NodeProperties.P42_assigned import P42_assigned


class E55_Type(E28_Conceptual_Object):
    hasType = RelationshipFrom(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P2_has_type",
        model=P2_has_type
    )
    had_general_purpose = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P21_had_general_purpose",
        model=P21_had_general_purpose)
    used_general_technique = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P32_used_general_technique",
        model=P32_used_general_technique
    )
    assigned = RelationshipFrom(
        ".E17_Type_Assignment.E17_Type_Assignment",
        "P42_assigned",
        model=P42_assigned)
    had_as_general_use = RelationshipFrom(
        ".E70_Thing.E70_Thing",
        "P101_had_as_general_use",
        model=P101_had_as_general_use)
    was_intended_for = RelationshipFrom(
        ".E71_Human_Made_Thing.E71_Human_Made_Thing",
        "P103_was_intended_for",
        model=P103_was_intended_for)
    used_object_of_type = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P125_used_object_of_type",
        model=P125_used_object_of_type
    )
    has_broader_term = RelationshipFrom(
        ".E55_Type.E55_Type",
        "P127_has_broader_term",
        model=P127_has_broader_term
    )
    created_type = RelationshipFrom(
        ".E83_Type_Creation.E83_Type_Creation",
        "P135_created_type",
        model=P135_created_type
    )
    exemplifies = RelationshipFrom(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P137_exemplifies",
        model=P137_exemplifies
    )
    defines_typical_parts_of = RelationshipFrom(
        ".E55_Type.E55_Type",
        "P150_defines_typical_parts_of",
        model=P150_defines_typical_parts_of
    )
    assigned_property_type = RelationshipFrom(
        ".E13_Attribute_Assignment",
        "P177_assigned_property_type",
        model=P177_assigned_property_type
    )

