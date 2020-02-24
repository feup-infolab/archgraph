from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeProperties.P72_has_language import P72_has_language


class E56_Language(E55_Type):
    has_language = RelationshipFrom(
        ".E33_Linguistic_Object.E33_Linguistic_Object",
        "P72_has_language",
        model=P72_has_language)

