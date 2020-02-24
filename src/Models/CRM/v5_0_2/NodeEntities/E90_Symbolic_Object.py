from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import \
    E72_Legal_Object
from src.Models.CRM.v5_0_2.NodeProperties.P106_is_composed_of import P106_is_composed_of


class E90_Symbolic_Object(E72_Legal_Object, E28_Conceptual_Object):
    is_composed_of = RelationshipFrom(
        ".E90_Symbolic_Object.E90_Symbolic_Object",
        "P106_is_composed_of",
        model=P106_is_composed_of)
