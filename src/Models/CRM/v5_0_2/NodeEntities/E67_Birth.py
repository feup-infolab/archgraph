from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import (
    E63_Beggining_of_Existence,
)
from src.Models.CRM.v5_0_2.NodeProperties.P96_by_mother import P96_by_mother
from src.Models.CRM.v5_0_2.NodeProperties.P97_from_father import P97_from_father
from src.Models.CRM.v5_0_2.NodeProperties.P98_brought_into_life import (
    P98_brought_into_life,
)


class E67_Birth(E63_Beggining_of_Existence):
    by_mother = RelationshipTo(
        ".E21_Person.E21_Person", "P96_by_mother", model=P96_by_mother
    )
    from_father = RelationshipTo(
        ".E21_Person.E21_Person", "P97_from_father", model=P97_from_father
    )
    brought_into_life = RelationshipTo(
        ".E21_Person.E21_Person", "P98_brought_into_life", model=P98_brought_into_life
    )
