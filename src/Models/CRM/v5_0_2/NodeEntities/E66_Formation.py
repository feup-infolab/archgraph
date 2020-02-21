from neomodel import (IntegerProperty, One, RelationshipTo, StringProperty,
                      StructuredNode, UniqueIdProperty, config)

from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import \
    E63_Beggining_of_Existence


class E66_Formation(E7_Activity, E63_Beggining_of_Existence):
    pass
