
from src.Models.CRM.v5_0_2.NodeEntities.E71_Human_Made_Thing import (
    E71_Human_Made_Thing,
    E71_Human_Made_ThingSchema,
)


class E28_Conceptual_ObjectSchema(E71_Human_Made_ThingSchema):
    pass


class E28_Conceptual_Object(E71_Human_Made_Thing):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E28_Conceptual_ObjectSchema()

        super().__init__(schema, *args, **kwargs)
