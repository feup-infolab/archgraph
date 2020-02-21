from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from DataObject.Date import Date
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdDateTime(StructuredRelCl):
    pass


class Interval(Date):
    startDateValue = RelationshipFrom(
        "Interval", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
    endDateValue = RelationshipFrom(
        "Interval", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
