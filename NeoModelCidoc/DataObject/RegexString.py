from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, RegexProperty)
from json import JSONEncoder
from DataObject.String import String
from NodeProperties.StructuredRelCl import StructuredRelCl


class RegexString(String):
    hasRegex = RegexProperty(unique_index=True, required=True)

