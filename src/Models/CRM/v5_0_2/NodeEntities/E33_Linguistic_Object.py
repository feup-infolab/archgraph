from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E73_Information_Object import \
    E73_Information_Object
from src.Models.CRM.v5_0_2.NodeProperties.P72_has_language import \
    P72_has_language
from src.Models.CRM.v5_0_2.NodeProperties.P73_has_translation import \
    P73_has_translation


class E33_Linguistic_Object(E73_Information_Object):
    has_translation = RelationshipTo(
        ".E33_Linguistic_Object.E33_Linguistic_Object",
        "P73_has_translation",
        model=P73_has_translation,
    )
    has_language = RelationshipTo(
        ".E56_Language.E56_Language", "P72_has_language", model=P72_has_language,
    )
