from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo,One,  RelationshipFrom, DateTimeProperty)
from json import JSONEncoder
from DataObject.Date import Date


class Instant(Date):
    timestamp = DateTimeProperty(unique_index=True, required=True)
