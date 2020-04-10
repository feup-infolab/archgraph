from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeProperties.P140_assigned_attribute_to import (
    P140_assigned_attribute_to,
)
from src.Models.CRM.v5_0_2.NodeProperties.P141_assigned import P141_assigned
from src.Models.CRM.v5_0_2.NodeProperties.P177_assigned_property_type import (
    P177_assigned_property_type,
)


class E13_Attribute_Assignment(E7_Activity):
    assigned_attribute_to = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity",
        "P140_assigned_attribute_to",
        model=P140_assigned_attribute_to,
    )
    assigned = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P141_assigned", model=P141_assigned,
    )
    assigned_property_type = RelationshipTo(
        ".E55_Type.E55_Type",
        "P177_assigned_property_type",
        model=P177_assigned_property_type,
    )
