from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import (
    E1_CRM_Entity,
    E1_CRM_EntitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P91_has_unit import P91_has_unit


#todo
class E54_DimensionSchema(E1_CRM_EntitySchema):
    #P91_has_unit = fields.List(fields.Nested("src.Models.CRM.v5_0_2.NodeEntities.E58_Measurement_Unit.E58_Measurement_UnitSchema"))
    pass


class E54_Dimension(E1_CRM_Entity):
    P91_has_unit = RelationshipTo(
        ".E58_Measurement_Unit.E58_Measurement_Unit", "P91_has_unit", model=P91_has_unit
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E54_DimensionSchema()

        super().__init__(schema, *args, **kwargs)
