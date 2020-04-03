from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import \
    E64_End_of_Existence
from src.Models.CRM.v5_0_2.NodeProperties.P100_was_death_of import \
    P100_was_death_of


class E69_Death(E64_End_of_Existence):
    was_death_of = RelationshipTo(
        ".E21_Person.E21_Person", "P100_was_death_of", model=P100_was_death_of
    )
