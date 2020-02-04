from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo,One, RelationshipFrom)
from json import JSONEncoder
from DataObject.DataObject import DataObject
from NodeProperties.StructuredRelCl import StructuredRelCl


class String(DataObject):
    stringValue = StringProperty(unique_index=True, required=True)

