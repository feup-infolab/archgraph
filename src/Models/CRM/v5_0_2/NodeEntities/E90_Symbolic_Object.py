from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E28_Conceptual_Object import \
    E28_Conceptual_Object
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import \
    E72_Legal_Object
from src.Models.CRM.v5_0_2.NodeProperties.P106_is_composed_of import \
    P106_is_composed_of
from src.Models.CRM.v5_0_2.NodeProperties.P128_carries import P128_carries
from src.Models.CRM.v5_0_2.NodeProperties.P142_used_constituent import \
    P142_used_constituent
from src.Models.CRM.v5_0_2.NodeProperties.P165_incorporates import \
    P165_incorporates


class E90_Symbolic_Object(E72_Legal_Object, E28_Conceptual_Object):
    is_composed_of = RelationshipFrom(
        ".E90_Symbolic_Object.E90_Symbolic_Object",
        "P106_is_composed_of",
        model=P106_is_composed_of,
    )
    carries = RelationshipFrom(
        ".E18_Physical_Thing.E18_Physical_Thing", "P128_carries", model=P128_carries
    )
    used_constituent = RelationshipFrom(
        ".E15_Identifier_Assignment.E15_Identifier_Assignment",
        "P142_used_constituent",
        model=P142_used_constituent,
    )
    incorporates = RelationshipFrom(
        ".E73_Information_Object.E73_Information_Object",
        "P165_incorporates",
        model=P165_incorporates,
    )
