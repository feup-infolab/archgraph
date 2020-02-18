from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    One,
)
from src.Models.CRM.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.NodeEntities.E58_Measurement_Unit import E58_Measurement_Unit


class E98_Currency(E55_Type, E58_Measurement_Unit):
    pass
