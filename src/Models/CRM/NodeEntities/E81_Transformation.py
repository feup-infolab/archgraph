from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
)

from src.Models.CRM.NodeEntities.E63_Beggining_of_Existence import E63_Beggining_of_Existence
from src.Models.CRM.NodeEntities.E64_End_of_Existence import E64_End_of_Existence


class E81_Transformation(E63_Beggining_of_Existence, E64_End_of_Existence):
    pass
