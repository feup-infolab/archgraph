from marshmallow import fields
from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import (
    E73_Information_Object,
    E73_Information_ObjectSchema,
)
from src.Models.CRM.v5_0_2.NodeProperties.P70_documents import P70_documents
from src.GCF.decorators.OntologyClass import decorator_schema


@decorator_schema
class E31_DocumentSchema(E73_Information_ObjectSchema):
    documents = fields.List(
        fields.Nested(
            "src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity.E1_CRM_EntitySchema"
        )
    )


class E31_Document(E73_Information_Object):
    documents = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P70_documents", model=P70_documents
    )

    def __init__(self, schema=None, *args, **kwargs):
        if schema is None:
            schema = E31_DocumentSchema()

        super().__init__(schema, *args, **kwargs)
