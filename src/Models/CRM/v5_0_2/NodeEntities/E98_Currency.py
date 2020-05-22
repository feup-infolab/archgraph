from src.Models.CRM.v5_0_2.NodeEntities.E58_Measurement_Unit import E58_Measurement_Unit, E58_Measurement_UnitSchema
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E98_CurrencySchema(E58_Measurement_UnitSchema, E55_TypeSchema):
    pass


class E98_Currency(E58_Measurement_Unit, E55_Type):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E98_CurrencySchema()

        super().__init__(schema, *args, **kwargs)
