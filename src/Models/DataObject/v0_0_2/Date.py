from src.Models.DataObject.v0_0_2.DataObject import DataObject, Schema


class Schema(Schema):
    pass


class Date(DataObject):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = Schema()

        super().__init__(schema, *args, **kwargs)
