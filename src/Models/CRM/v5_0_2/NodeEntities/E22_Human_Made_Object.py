from src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object import E19_Physical_Object, E19_Physical_ObjectSchema
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import (
    E24_Physical_Human_Made_Thing,
    E24_Physical_Human_Made_ThingSchema)


#Todo verificar
class E22_Human_Made_ObjectSchema(E19_Physical_ObjectSchema, E24_Physical_Human_Made_ThingSchema):
    pass


class E22_Human_Made_Object(E19_Physical_Object, E24_Physical_Human_Made_Thing):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E22_Human_Made_ObjectSchema()

        super().__init__(schema, *args, **kwargs)

