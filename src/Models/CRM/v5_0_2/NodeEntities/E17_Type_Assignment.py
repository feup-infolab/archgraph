from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import (
    E13_Attribute_Assignment,
)
from src.Models.CRM.v5_0_2.NodeProperties.P41_classified import P41_classified
from src.Models.CRM.v5_0_2.NodeProperties.P42_assigned import P42_assigned


class E17_Type_Assignment(E13_Attribute_Assignment):
    classified = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P41_classified", model=P41_classified,
    )
    assigned = RelationshipTo(".E55_Type.E55_Type", "P42_assigned", model=P42_assigned)
