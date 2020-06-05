from marshmallow import Schema, fields

from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import (
    E1_CRM_Entity,
    E1_CRM_EntitySchema,
)


# todo class super
@decorator_schema
class E77_Persistent_ItemSchema(Schema):
    uid = fields.String()
    name = fields.String(required=True)


class E77_Persistent_Item(E1_CRM_Entity):
    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E77_Persistent_ItemSchema()

        super().__init__(schema, *args, **kwargs)
