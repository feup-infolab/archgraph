from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E33_Linguistic_Object import \
    E33_Linguistic_Object
from src.Models.CRM.v5_0_2.NodeProperties.P102_has_title import P102_has_title


class E35_Title(E33_Linguistic_Object):
    has_title = RelationshipFrom(
        ".E71_Human_Made_Thing.E71_Human_Made_Thing", "P102_has_title", model=P102_has_title
    )
    pass
