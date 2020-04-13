from src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object import E19_Physical_Object, E19_Physical_ObjectSchema


class E20_Biological_ObjectSchema(E19_Physical_ObjectSchema):
    pass


class E20_Biological_Object(E19_Physical_Object):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E20_Biological_ObjectSchema()

        super().__init__(schema, *args, **kwargs)