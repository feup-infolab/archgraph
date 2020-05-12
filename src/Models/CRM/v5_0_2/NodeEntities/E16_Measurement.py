from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E13_Attribute_Assignment import (
    E13_Attribute_Assignment,
    E13_Attribute_AssignmentSchema)
from src.Models.CRM.v5_0_2.NodeProperties.P39_measured import P39_measured
from src.Models.CRM.v5_0_2.NodeProperties.P40_observed_dimension import (
    P40_observed_dimension,
)


@decorator_schema
class E16_MeasurementSchema(E13_Attribute_AssignmentSchema):
    measured = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema")
    )
    observed_dimension = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension.E54_DimensionSchema")
    )


class E16_Measurement(E13_Attribute_Assignment):
    measured = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P39_measured", model=P39_measured
    )
    observed_dimension = RelationshipTo(
        ".E54_Dimension.E54_Dimension",
        "P40_observed_dimension",
        model=P40_observed_dimension,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E16_MeasurementSchema()

        super().__init__(schema, *args, **kwargs)
