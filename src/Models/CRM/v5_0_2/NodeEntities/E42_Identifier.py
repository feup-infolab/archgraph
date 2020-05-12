from src.Models.CRM.v5_0_2.NodeEntities.E41_Appellation import (
    E41_Appellation,
    E41_AppellationSchema,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E42_IdentifierSchema(E41_AppellationSchema):
    pass


class E42_Identifier(E41_Appellation):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E42_IdentifierSchema()

        super().__init__(schema, *args, **kwargs)
