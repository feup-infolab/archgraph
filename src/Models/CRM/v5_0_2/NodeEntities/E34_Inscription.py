from src.Models.CRM.v5_0_2.NodeEntities.E37_Mark import E37_Mark, E37_MarkSchema
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E34_InscriptionSchema(E37_MarkSchema):
    pass


class E34_Inscription(E37_Mark):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E34_InscriptionSchema()

        super().__init__(schema, *args, **kwargs)
