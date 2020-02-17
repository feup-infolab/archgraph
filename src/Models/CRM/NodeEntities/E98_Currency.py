from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
)
from NodeEntities.E55_Type import E55_Type
from NodeEntities.E58_Measurement_Unit import E58_Measurement_Unit


class E98_Currency(E55_Type, E58_Measurement_Unit):
    pass
