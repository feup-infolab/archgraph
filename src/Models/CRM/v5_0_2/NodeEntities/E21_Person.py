from neomodel import RelationshipTo
from src.Models.CRM.v5_0_2.NodeEntities.E20_Biological_Object import (
    E20_Biological_Object,
)
from src.Models.CRM.v5_0_2.NodeProperties.P98_brought_into_life import (
    P98_brought_into_life,
)
from src.Models.CRM.v5_0_2.NodeProperties.P152_has_parent import P152_has_parent


class E21_Person(E20_Biological_Object):
    has_parent = RelationshipTo(
        ".E21_Person.E21_Person", "P152_has_parent", model=P152_has_parent
    )
