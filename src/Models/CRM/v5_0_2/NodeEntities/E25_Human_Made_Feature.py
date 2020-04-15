from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import (
    E24_Physical_Human_Made_Thing,
    E24_Physical_Human_Made_ThingSchema)
from src.Models.CRM.v5_0_2.NodeEntities.E26_Physical_Feature import E26_Physical_Feature, E26_Physical_FeatureSchema


#Todo verificar
class E25_Human_Made_FeatureSchema(E24_Physical_Human_Made_ThingSchema, E26_Physical_FeatureSchema):
    pass


class E25_Human_Made_Feature(E24_Physical_Human_Made_Thing, E26_Physical_Feature):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E25_Human_Made_FeatureSchema()

        super().__init__(schema, *args, **kwargs)
