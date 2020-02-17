from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)
from json import JSONEncoder
from DataObject.GeospatialCoordinates import GeospatialCoordinates


class Polygon(GeospatialCoordinates):
    pass
