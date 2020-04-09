
from src.Models.CRM.v5_0_2.NodeEntities.E89_Propositional_Object import \
    E89_Propositional_Object, E89_Propositional_ObjectSchema


class E30_RightSchema(E89_Propositional_ObjectSchema):
    pass


class E30_Right(E89_Propositional_Object):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E30_RightSchema()

        super().__init__(schema, *args, **kwargs)
