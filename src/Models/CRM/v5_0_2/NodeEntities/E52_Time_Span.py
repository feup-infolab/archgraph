from marshmallow import Schema, fields
from neomodel import DateTimeFormatProperty, RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import (
    E1_CRM_Entity,
    E1_CRM_EntitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P86_falls_within import P86_falls_within
from src.Models.CRM.v5_0_2.NodeProperties.P191_had_duration import P191_had_duration
from src.GCF.decorators.OntologyClass import decorator_schema, ontology_class


@decorator_schema
class E52_Time_SpanSchema(E1_CRM_EntitySchema):
    date = fields.Date(required=True)
    P86_falls_within = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span.E52_Time_SpanSchema"))
    P191_had_duration = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension.E54_DimensionSchema"))


# todo
class E52_Time_Span(E1_CRM_Entity):
    date = DateTimeFormatProperty(format="%Y-%m-%d", unique_index=True, required=True)
    P86_falls_within = RelationshipTo(
        ".E52_Time_Span.E52_Time_Span", "P86_falls_within", model=P86_falls_within
    )
    P191_had_duration = RelationshipTo(
        ".E54_Dimension.E54_Dimension", "P191_had_duration", model=P191_had_duration
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E52_Time_SpanSchema()

        super().__init__(schema, *args, **kwargs)
