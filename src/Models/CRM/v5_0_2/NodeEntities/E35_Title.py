from marshmallow import Schema

from src.Models.CRM.v5_0_2.NodeEntities.E33_Linguistic_Object import \
    E33_Linguistic_Object


class E35_TitleSchema(Schema):
    pass


class E35_Title(E33_Linguistic_Object):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E35_TitleSchema()

        super().__init__(schema, *args, **kwargs)
