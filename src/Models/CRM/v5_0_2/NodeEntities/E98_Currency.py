from neomodel import (IntegerProperty, One, RelationshipTo, StringProperty,
                      StructuredNode, UniqueIdProperty, config)

from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeEntities.E58_Measurement_Unit import \
    E58_Measurement_Unit


class E98_Currency(E55_Type, E58_Measurement_Unit):
    pass
