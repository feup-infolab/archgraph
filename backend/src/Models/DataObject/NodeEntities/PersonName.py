from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One, RelationshipFrom)
from json import JSONEncoder
from DataObject.AuthorityString import AuthorityString
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class PersonName(AuthorityString):
    name = StringProperty(unique_index=True, required=True)

