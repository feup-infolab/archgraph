from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema


class ARE5_Date_TypeSchema(E55_TypeSchema):
    pass


class ARE5_Date_Type(E55_Type):
    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE5_Date_TypeSchema()

        super().__init__(schema, *args, **kwargs)
