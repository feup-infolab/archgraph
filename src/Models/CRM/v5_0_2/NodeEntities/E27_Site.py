from src.Models.CRM.v5_0_2.NodeEntities.E26_Physical_Feature import (
    E26_Physical_Feature,
    E26_Physical_FeatureSchema,
)
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E27_SiteSchema(E26_Physical_FeatureSchema):
    pass


class E27_Site(E26_Physical_Feature):
    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E27_SiteSchema()

        super().__init__(schema, *args, **kwargs)
