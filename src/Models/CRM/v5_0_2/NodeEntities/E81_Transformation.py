from neomodel import (IntegerProperty, RelationshipTo, StringProperty,
                      StructuredNode, UniqueIdProperty, config)

from src.Models.CRM.v5_0_2.NodeEntities.E63_Beggining_of_Existence import \
    E63_Beggining_of_Existence
from src.Models.CRM.v5_0_2.NodeEntities.E64_End_of_Existence import \
    E64_End_of_Existence


class E81_Transformation(E63_Beggining_of_Existence, E64_End_of_Existence):
    pass