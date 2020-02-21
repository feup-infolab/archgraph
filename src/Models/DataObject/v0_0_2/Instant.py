from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from DataObject.Date import Date
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdDateTime(StructuredRelCl):
    pass


class Instant(Date):
    timestamp = RelationshipFrom(
        "Instant", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
