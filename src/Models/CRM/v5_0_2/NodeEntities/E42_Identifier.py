from marshmallow import Schema
from src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation import E41_Appellation


class E42_IdentifierSchema(Schema):
    pass


class E42_Identifier(E41_Appellation):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E42_IdentifierSchema()

        super().__init__(schema, *args, **kwargs)
