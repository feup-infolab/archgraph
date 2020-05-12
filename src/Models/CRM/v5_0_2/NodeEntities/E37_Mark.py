from src.Models.CRM.v5_0_2.NodeEntities.E36_Visual_Item import E36_Visual_Item, E36_Visual_ItemSchema
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E37_MarkSchema(E36_Visual_ItemSchema):
    pass


class E37_Mark(E36_Visual_Item):

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E37_MarkSchema()

        super().__init__(schema, *args, **kwargs)
