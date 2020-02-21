from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from DataObject.DataObject import DataObject
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdString(StructuredRelCl):
    pass


class String(DataObject):
    stringValue = RelationshipFrom(
        "String", "xsdString", cardinality=One, model=xsdString
    )
