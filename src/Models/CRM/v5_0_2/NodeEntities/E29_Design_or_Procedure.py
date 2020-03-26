from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import \
    E73_Information_Object
from src.Models.CRM.v5_0_2.NodeProperties.P33_used_specific_technique import \
    P33_used_specific_technique
from src.Models.CRM.v5_0_2.NodeProperties.P69_has_association_with import \
    P69_has_association_with
from src.Models.CRM.v5_0_2.NodeProperties.P187_has_production_plan import \
    P187_has_production_plan


class E29_Design_or_Procedure(E73_Information_Object):
    used_specific_technique = RelationshipFrom(
        ".E7_Activity.E7_Activity",
        "P33_used_specific_technique",
        model=P33_used_specific_technique,
    )
    has_association_with = RelationshipFrom(
        ".E29_Design_or_Procedure.E29_Design_or_Procedure",
        "P69_has_association_with",
        model=P69_has_association_with,
    )
    has_production_plan = RelationshipFrom(
        ".E99_Product_Type.E99_Product_Type",
        "P187_has_production_plan",
        model=P187_has_production_plan,
    )
