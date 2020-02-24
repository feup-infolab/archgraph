from neomodel import RelationshipFrom, StructuredRel
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object
from ..NodeProperties.P137_exemplifies import P137_exemplifies
from ..NodeProperties.P21_had_general_purpose import P21_had_general_purpose
from ..NodeProperties.P2_has_type import P2_has_type
from ..NodeProperties.P32_used_general_technique import P32_used_general_technique


class E55_Type(E28_Conceptual_Object):
    hasType = RelationshipFrom(E1_CRM_Entity, "P2_has_type", model=P2_has_type)
    exemplifies = RelationshipFrom(
        E1_CRM_Entity, "P137_exemplifies", model=P137_exemplifies
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
