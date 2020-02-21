from neomodel import (IntegerProperty, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from DataObject.GeospatialCoordinates import GeospatialCoordinates


class Polygon(GeospatialCoordinates):
    pass
