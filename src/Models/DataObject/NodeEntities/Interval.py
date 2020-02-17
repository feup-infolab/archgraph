from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
    DateTimeProperty,
)
from json import JSONEncoder
from DataObject.Date import Date


class Interval(Date):
    startDateValue = DateTimeProperty(unique_index=True, required=True)
    endDateValue = DateTimeProperty(unique_index=True, required=True)
