from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from json import JSONEncoder
from DataObject.AuthorityString import AuthorityString
from NodeProperties.StructuredRelCl import StructuredRelCl

class xsdString(StructuredRelCl):
    pass

class PersonName(AuthorityString):
    name = RelationshipFrom('Approximate', 'xsdString', model=xsdString)

