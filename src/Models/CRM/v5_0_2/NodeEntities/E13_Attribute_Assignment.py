from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import (
    E7_Activity,
    E7_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P140_assigned_attribute_to import (
    P140_assigned_attribute_to,
)
from src.Models.CRM.v5_0_2.NodeProperties.P141_assigned import P141_assigned
from src.Models.CRM.v5_0_2.NodeProperties.P177_assigned_property_type import (
    P177_assigned_property_type,
)


@decorator_schema
class E13_Attribute_AssignmentSchema(E7_ActivitySchema):
    assigned_attribute_to = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema"
        )
    )
    assigned = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema"
        )
    )
    assigned_property_type = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema")
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

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E13_Attribute_AssignmentSchema()

        super().__init__(schema, *args, **kwargs)
