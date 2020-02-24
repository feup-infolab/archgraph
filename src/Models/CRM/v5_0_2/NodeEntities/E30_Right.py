from neomodel import RelationshipFrom

from src.Models.CRM.v5_0_2.NodeEntities.E89_Propositional_Object import \
    E89_Propositional_Object
from src.Models.CRM.v5_0_2.NodeProperties.P75_possesses import P75_possesses


class E30_Right(E89_Propositional_Object):
    possesses = RelationshipFrom(
        ".E39_Actor.E39_Actor",
        "P75_possesses",
        model=P75_possesses)

