from marshmallow import Schema
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity


class E77_Persistent_ItemSchema(Schema):
    pass


class E77_Persistent_Item(E1_CRM_Entity):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E77_Persistent_ItemSchema()

        super().__init__(schema, *args, **kwargs)

