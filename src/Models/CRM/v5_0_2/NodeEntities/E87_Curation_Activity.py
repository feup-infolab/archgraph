from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity, E7_ActivitySchema
from src.Models.CRM.v5_0_2.NodeProperties.P147_curated import P147_curated
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E87_Curation_ActivitySchema(E7_ActivitySchema):
    curated = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E78_Curated_Holding.E78_Curated_HoldingSchema")
    )


class E87_Curation_Activity(E7_Activity):
    curated = RelationshipTo(
        ".E78_Curated_Holding.E78_Curated_Holding", "P147_curated", model=P147_curated,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E87_Curation_ActivitySchema()

        super().__init__(schema, *args, **kwargs)
