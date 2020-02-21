from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from DataObject.Date import Date
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdDateTime(StructuredRelCl):
    pass


class Approximate(Date):
    approximateDateValue = RelationshipFrom(
        "Approximate", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
