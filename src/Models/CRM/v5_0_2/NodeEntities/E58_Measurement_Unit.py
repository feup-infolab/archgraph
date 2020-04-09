from marshmallow import Schema

from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type


class E58_Measurement_UnitSchema(Schema):
    pass


class E58_Measurement_Unit(E55_Type):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E58_Measurement_UnitSchema()

        super().__init__(schema, *args, **kwargs)
