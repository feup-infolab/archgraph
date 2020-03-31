from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E89_Propositional_Object import \
    E89_Propositional_Object
from src.Models.CRM.v5_0_2.NodeProperties.P75_possesses import P75_possesses
from src.Models.CRM.v5_0_2.NodeProperties.P104_is_subject_to import \
    P104_is_subject_to


class E30_Right(E89_Propositional_Object):
    possesses = RelationshipFrom(
        ".E39_Actor.E39_Actor", "P75_possesses", model=P75_possesses
    )
    is_subject_to = RelationshipFrom(
        ".E72_Legal_Object.E72_Legal_Object",
        "P104_is_subject_to",
        model=P104_is_subject_to,
    )
