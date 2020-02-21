from neomodel import (One, RelationshipFrom, StructuredRel)

from .Date import Date


class xsdDateTime(StructuredRel):
    pass


class Instant(Date):
    timestamp = RelationshipFrom(
        "Instant", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
