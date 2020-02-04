from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, One)
from json import JSONEncoder
from DataObject.Date import Date
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdDateTime(StructuredRelCl):
    pass


class Interval(Date):
    startDateValue = RelationshipFrom('Interval', 'xsdDateTime', cardinality=One, model=xsdDateTime)
    endDateValue = RelationshipFrom('Interval', 'xsdDateTime', cardinality=One, model=xsdDateTime)

