from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema


class ARE7_NameSchema(E55_TypeSchema):
    pass


class ARE7_Name(E55_Type):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE7_NameSchema()

        super().__init__(schema, *args, **kwargs)
