from src.Models.DataObject.v0_0_2.DataObject import DataObject, DataObjectSchema
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class IntegerSchema(DataObjectSchema):
    pass


class Integer(DataObject):
    pass

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = IntegerSchema()

        super().__init__(schema, *args, **kwargs)
