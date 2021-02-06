from src.Models.DataObject.v0_0_2.DataObject import DataObject, DataObjectSchema
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class DateSchema(DataObjectSchema):
    pass


class Date(DataObject):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = DateSchema()

        super().__init__(schema, *args, **kwargs)
