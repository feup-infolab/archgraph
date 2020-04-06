from marshmallow import Schema

from src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object import \
    E90_Symbolic_Object


class E41_AppellationSchema(Schema):
    pass


class E41_Appellation(E90_Symbolic_Object):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E41_AppellationSchema()

        super().__init__(schema, *args, **kwargs)
