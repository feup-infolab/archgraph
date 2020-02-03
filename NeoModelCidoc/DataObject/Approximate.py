from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)
from json import JSONEncoder
from DataObject.Date import Date
from NodeProperties.StructuredRelCl import StructuredRelCl

class xsdDateTime(StructuredRelCl):
    pass


class Approximate(Date):
    approximateDateValue = RelationshipFrom('Approximate', 'xsdDateTime', model=xsdDateTime)

