from src.Models.DataObject.v0_0_2.DataObject import DataObject, DataObjectSchema


class DateSchema(DataObjectSchema):
    pass


class Date(DataObject):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = DateSchema()

        super().__init__(schema, *args, **kwargs)
