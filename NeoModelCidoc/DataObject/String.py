from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo,One, RelationshipFrom)
from json import JSONEncoder
from DataObject.DataObject import DataObject
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdString(StructuredRelCl):
    pass


class String(DataObject):
    stringValue = RelationshipFrom('String', 'xsdString', cardinality=One, model=xsdString)

