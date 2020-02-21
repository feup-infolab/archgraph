from neomodel import (IntegerProperty, One, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)

from DataObject.AuthorityString import AuthorityString
from NodeProperties.StructuredRelCl import StructuredRelCl


class xsdString(StructuredRelCl):
    pass


class PersonName(AuthorityString):
    name = RelationshipFrom(
        "Approximate", "xsdString", cardinality=One, model=xsdString
    )
