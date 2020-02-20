from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)
from json import JSONEncoder


class DataObject(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
