from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E65_Creation import E65_Creation, E65_CreationSchema
from src.Models.CRM.v5_0_2.NodeProperties.P135_created_type import P135_created_type
from src.Models.CRM.v5_0_2.NodeProperties.P136_was_based_on import P136_was_based_on
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E83_Type_CreationSchema(E65_CreationSchema):
    was_based_on = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema")
    )
    created_type = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E55_Type.E55_TypeSchema")
    )


class E83_Type_Creation(E65_Creation):
    was_based_on = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P136_was_based_on", model=P136_was_based_on,
    )
    created_type = RelationshipTo(
        ".E55_Type.E55_Type", "P135_created_type", model=P135_created_type,
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E83_Type_CreationSchema()

        super().__init__(schema, *args, **kwargs)
