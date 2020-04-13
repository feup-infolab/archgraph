from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E31_Document import E31_Document, E31_DocumentSchema
from src.Models.CRM.v5_0_2.NodeProperties.P71_lists import P71_lists


class E32_Authority_DocumentSchema(E31_DocumentSchema):
    documents = fields.List(fields.Nested(
        "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema")
    )


class E32_Authority_Document(E31_Document):
    lists = RelationshipTo(".E1_CRM_Entity.E1_CRM_Entity", "P71_lists", model=P71_lists)

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E32_Authority_DocumentSchema()

        super().__init__(schema, *args, **kwargs)
