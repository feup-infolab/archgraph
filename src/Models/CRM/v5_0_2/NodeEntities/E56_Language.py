from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema


class E56_LanguageSchema(E55_TypeSchema):
    pass


class E56_Language(E55_Type):
    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E56_LanguageSchema()

        super().__init__(schema, *args, **kwargs)
