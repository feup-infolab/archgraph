from src.Models.DataObject.v0_0_2.DataObject import DataObject, DataObjectSchema


class DecimalSchema(DataObjectSchema):
    pass


class Decimal(DataObject):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = DecimalSchema()

        super().__init__(schema, *args, **kwargs)
