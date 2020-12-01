from marshmallow import fields
from neomodel import RelationshipTo
from src.GCF.decorators.OntologyClass import decorator_schema
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import (
    E7_Activity,
    E7_ActivitySchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P31_has_modified import P31_has_modified
from src.Models.CRM.v5_0_2.NodeProperties.P126_employed import P126_employed


@decorator_schema
class E11_ModificationSchema(E7_ActivitySchema):
    employed = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E57_Material.E57_MaterialSchema"
        )
    )
    has_modified = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing.E18_Physical_ThingSchema"
        )
    )


class E11_Modification(E7_Activity):
    employed = RelationshipTo(
        ".E57_Material.E57_Material", "P126_employed", model=P126_employed
    )
    has_modified = RelationshipTo(
        ".E18_Physical_Thing.E18_Physical_Thing",
        "P31_has_modified",
        model=P31_has_modified,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E11_ModificationSchema()

        super().__init__(schema, *args, **kwargs)
