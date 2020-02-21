from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from DataObject.String import String
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdString(StructuredRelCl):
    pass


class RegexString(String):
    hasRegex = RelationshipFrom(
        "RegexString", "xsdString", cardinality=One, model=xsdString
    )
