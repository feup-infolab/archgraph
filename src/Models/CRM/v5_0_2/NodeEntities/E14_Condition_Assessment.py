from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import (
    E13_Attribute_Assignment,
    E13_Attribute_AssignmentSchema)
from src.Models.CRM.v5_0_2.NodeProperties.P34_concerned import P34_concerned
from src.Models.CRM.v5_0_2.NodeProperties.P35_has_identified import P35_has_identified


@decorator_schema
class E14_Condition_AssessmentSchema(E13_Attribute_AssignmentSchema):
    has_identified = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E3_Condition_State.E3_Condition_StateSchema")
    )
    concerned = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema")
    )


class E14_Condition_Assessment(E13_Attribute_Assignment):
    has_identified = RelationshipTo(
        ".E3_Condition_State.E3_Condition_State",
        "P35_has_identified",
        model=P35_has_identified,
    )
    concerned = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing", "P34_concerned", model=P34_concerned,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E14_Condition_AssessmentSchema()

        super().__init__(schema, *args, **kwargs)
