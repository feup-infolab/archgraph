from marshmallow import Schema, fields

from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type


class E57_MaterialSchema(Schema):
    pass


class E57_Material(E55_Type):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E57_MaterialSchema()

        super().__init__(schema, *args, **kwargs)
