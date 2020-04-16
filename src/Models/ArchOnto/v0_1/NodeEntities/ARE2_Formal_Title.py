from src.Models.CRM.v5_0_2.NodeEntities.E35_Title import E35_Title, E35_TitleSchema


class ARE2_Formal_TitleSchema(E35_TitleSchema):
    pass


class ARE2_Formal_Title(E35_Title):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE2_Formal_TitleSchema()

        super().__init__(schema, *args, **kwargs)
