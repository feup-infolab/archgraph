from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E31_Document import E31_Document
from src.Models.CRM.v5_0_2.NodeProperties.P71_lists import P71_lists


class E32_Authority_Document(E31_Document):
    lists = RelationshipTo(".E1_CRM_Entity.E1_CRM_Entity", "P71_lists", model=P71_lists)
