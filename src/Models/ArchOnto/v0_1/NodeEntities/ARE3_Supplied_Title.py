from src.Models.CRM.v5_0_2.NodeEntities.E35_Title import E35_Title, E35_TitleSchema


class ARE3_Supplied_TitleSchema(E35_TitleSchema):
    pass


class ARE3_Supplied_Title(E35_Title):
    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE3_Supplied_TitleSchema()

        super().__init__(schema, *args, **kwargs)
