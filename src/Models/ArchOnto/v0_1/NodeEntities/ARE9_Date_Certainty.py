from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema


class ARE9_Date_CertaintySchema(E55_TypeSchema):
    pass


class ARE9_Date_Certainty(E55_Type):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE9_Date_CertaintySchema()

        super().__init__(schema, *args, **kwargs)
