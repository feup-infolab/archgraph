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
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class Approximate(Date):
    approximateDateValue = DateTimeProperty(unique_index=True, required=True)
