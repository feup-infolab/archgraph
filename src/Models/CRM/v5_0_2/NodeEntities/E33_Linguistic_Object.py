from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import \
    E73_Information_Object
from src.Models.CRM.v5_0_2.NodeProperties.P73_has_translation import \
    P73_has_translation


class E33_Linguistic_Object(E73_Information_Object):
    has_translation = RelationshipFrom(
        ".E33_Linguistic_Object.E33_Linguistic_Object",
        "P73_has_translation",
        model=P73_has_translation,
    )
