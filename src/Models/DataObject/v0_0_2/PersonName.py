from neomodel import (One, RelationshipFrom, StructuredRel)

from .AuthorityString import AuthorityString


class xsdString(StructuredRel):
    pass


class PersonName(AuthorityString):
    name = RelationshipFrom(
        "Approximate", "xsdString", cardinality=One, model=xsdString
    )
