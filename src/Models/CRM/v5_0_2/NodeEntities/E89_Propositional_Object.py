from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object
from src.Models.CRM.v5_0_2.NodeProperties.P148_has_component import \
    P148_has_component


class E89_Propositional_Object(E28_Conceptual_Object):
    curated = RelationshipFrom(
        ".E89_Propositional_Object.E89_Propositional_Object",
        "P148_has_component",
        model=P148_has_component,
    )
