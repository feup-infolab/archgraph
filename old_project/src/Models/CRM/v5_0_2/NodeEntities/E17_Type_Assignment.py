from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import (
    E13_Attribute_Assignment,
    E13_Attribute_AssignmentSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P41_classified import P41_classified
from src.Models.CRM.v5_0_2.NodeProperties.P42_assigned import P42_assigned


@decorator_schema
class E17_Type_AssignmentSchema(E13_Attribute_AssignmentSchema):
    classified = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema"
        )
    )
    assigned = fields.List(
        fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema")
    )


class E17_Type_Assignment(E13_Attribute_Assignment):
    classified = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P41_classified", model=P41_classified,
    )
    assigned = RelationshipTo(".E55_Type.E55_Type", "P42_assigned", model=P42_assigned)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E17_Type_AssignmentSchema()

        super().__init__(schema, *args, **kwargs)
