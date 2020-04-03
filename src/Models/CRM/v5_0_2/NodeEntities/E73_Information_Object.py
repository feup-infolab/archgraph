from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E89_Propositional_Object import \
    E89_Propositional_Object
from src.Models.CRM.v5_0_2.NodeEntities.E90_Symbolic_Object import \
    E90_Symbolic_Object
from src.Models.CRM.v5_0_2.NodeProperties.P165_incorporates import \
    P165_incorporates


class E73_Information_Object(E89_Propositional_Object, E90_Symbolic_Object):
    incorporates = RelationshipTo(
        ".E73_Information_Object.E73_Information_Object",
        "P165_incorporates",
        model=P165_incorporates,
    )
