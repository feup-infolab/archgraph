from neomodel import RelationshipFrom
from src.Models.CRM.v5_0_2.NodeEntities.E20_Biological_Object import \
    E20_Biological_Object
from src.Models.CRM.v5_0_2.NodeProperties.P96_by_mother import P96_by_mother
from src.Models.CRM.v5_0_2.NodeProperties.P97_from_father import \
    P97_from_father
from src.Models.CRM.v5_0_2.NodeProperties.P98_brought_into_life import \
    P98_brought_into_life
from src.Models.CRM.v5_0_2.NodeProperties.P100_was_death_of import \
    P100_was_death_of
from src.Models.CRM.v5_0_2.NodeProperties.P152_has_parent import \
    P152_has_parent


class E21_Person(E20_Biological_Object):
    by_mother = RelationshipFrom(
        ".E67_Birth.E67_Birth", "P96_by_mother", model=P96_by_mother
    )
    from_father = RelationshipFrom(
        ".E67_Birth.E67_Birth", "P97_from_father", model=P97_from_father
    )
    brought_into_life = RelationshipFrom(
        ".E67_Birth.E67_Birth", "P98_brought_into_life", model=P98_brought_into_life
    )
    was_death_of = RelationshipFrom(
        ".E69_Death.E69_Death", "P100_was_death_of", model=P100_was_death_of
    )
    has_parent = RelationshipFrom(
        ".E21_Person.E21_Person", "P152_has_parent", model=P152_has_parent
    )
