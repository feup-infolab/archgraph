from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import (
    E73_Information_Object,
)
from src.Models.CRM.v5_0_2.NodeProperties.P70_documents import P70_documents


class E31_Document(E73_Information_Object):
    documents = RelationshipTo(
        ".E1_CRM_Entity.E1_CRM_Entity", "P70_documents", model=P70_documents
    )
