from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import (
    E13_Attribute_Assignment,
    E13_Attribute_AssignmentSchema)
from src.Models.CRM.v5_0_2.NodeProperties.P37_assigned import P37_assigned
from src.Models.CRM.v5_0_2.NodeProperties.P38_deassigned import P38_deassigned
from src.Models.CRM.v5_0_2.NodeProperties.P142_used_constituent import (
    P142_used_constituent,
)


@decorator_schema
class E15_Identifier_AssignmentSchema(E13_Attribute_AssignmentSchema):
    used_constituent = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object.E90_Symbolic_ObjectSchema")
    )
    deassigned = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E42_Identifier.E42_IdentifierSchema")
    )
    assigned = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E42_Identifier.E42_IdentifierSchema")
    )


class E15_Identifier_Assignment(E13_Attribute_Assignment):
    used_constituent = RelationshipTo(
        ".E90_Symbolic_Object.E90_Symbolic_Object",
        "P142_used_constituent",
        model=P142_used_constituent,
    )
    deassigned = RelationshipTo(
        ".E42_Identifier.E42_Identifier", "P38_deassigned", model=P38_deassigned,
    )
    assigned = RelationshipTo(
        ".E42_Identifier.E42_Identifier", "P37_assigned", model=P37_assigned,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E15_Identifier_AssignmentSchema()

        super().__init__(schema, *args, **kwargs)
