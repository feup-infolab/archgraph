from marshmallow import Schema, fields
from neomodel import One, RelationshipTo, ZeroOrOne
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import (
    E2_Temporal_Entity,
    E2_Temporal_EntitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P5_consists_of import P5_consists_of


@decorator_schema
class E3_Condition_StateSchema(E2_Temporal_EntitySchema):
    P5_consists_of = fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E3_Condition_State.E3_Condition_StateSchema",
        exclude=("P5_consists_of",),
    )


class E3_Condition_State(E2_Temporal_Entity):
    P5_consists_of = RelationshipTo(
        ".E3_Condition_State.E3_Condition_State",
        "P5_consists_of",
        cardinality=ZeroOrOne,
        model=P5_consists_of,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E3_Condition_StateSchema()

        super().__init__(schema, *args, **kwargs)
