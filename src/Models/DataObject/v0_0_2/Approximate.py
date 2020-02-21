from neomodel import One, RelationshipFrom, StructuredRel

from .Date import Date


class xsdDateTime(StructuredRel):
    pass


class Approximate(Date):
    approximateDateValue = RelationshipFrom(
        "Approximate", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
