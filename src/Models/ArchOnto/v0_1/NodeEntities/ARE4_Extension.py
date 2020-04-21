from src.Models.CRM.v5_0_2.NodeEntities.E54_Dimension import E54_Dimension, E54_DimensionSchema


class ARE4_ExtensionSchema(E54_DimensionSchema):
    pass


class ARE4_Extension(E54_Dimension):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = ARE4_ExtensionSchema()

        super().__init__(schema, *args, **kwargs)
