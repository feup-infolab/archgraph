from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema
from src.Models.CRM.v5_0_2.NodeEntities.E58_Measurement_Unit import E58_Measurement_Unit


#todo
class E98_CurrencySchema(E55_TypeSchema):
    pass


class E98_Currency(E55_Type, E58_Measurement_Unit):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E98_CurrencySchema()

        super().__init__(schema, *args, **kwargs)
