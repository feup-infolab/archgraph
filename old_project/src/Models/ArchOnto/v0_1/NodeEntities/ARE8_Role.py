from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type, E55_TypeSchema


class ARE8_RoleSchema(E55_TypeSchema):
    pass


class ARE8_Role(E55_Type):
    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE8_RoleSchema()

        super().__init__(schema, *args, **kwargs)
