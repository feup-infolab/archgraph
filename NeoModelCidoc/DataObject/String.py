from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from json import JSONEncoder
from DataObject.DataObject import DataObject
from NodeProperties.StructuredRelCl import StructuredRelCl

class xsdString(StructuredRelCl):
    pass


class String(DataObject):
    stringValue = RelationshipFrom('String', 'xsdString', model=xsdString)

