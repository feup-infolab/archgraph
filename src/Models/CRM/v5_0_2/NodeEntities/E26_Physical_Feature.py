from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import E18_Physical_Thing, E18_Physical_ThingSchema


class E26_Physical_FeatureSchema(E18_Physical_ThingSchema):
    pass


class E26_Physical_Feature(E18_Physical_Thing):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E26_Physical_FeatureSchema()

        super().__init__(schema, *args, **kwargs)
