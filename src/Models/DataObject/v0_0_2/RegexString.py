from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
    One,
)
from json import JSONEncoder
from DataObject.String import String
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdString(StructuredRelCl):
    pass


class RegexString(String):
    hasRegex = RelationshipFrom(
        "RegexString", "xsdString", cardinality=One, model=xsdString
    )
