from src.Models.CRM.v5_0_2.NodeEntities.E33_Linguistic_Object import (
    E33_Linguistic_Object,
    E33_Linguistic_ObjectSchema,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E35_TitleSchema(E33_Linguistic_ObjectSchema):
    pass


class E35_Title(E33_Linguistic_Object):
    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E35_TitleSchema()

        super().__init__(schema, *args, **kwargs)
