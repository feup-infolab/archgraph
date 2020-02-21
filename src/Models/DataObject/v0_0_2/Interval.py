from neomodel import One, RelationshipFrom, StructuredRel

from .Date import Date


class xsdDateTime(StructuredRel):
    pass


class Interval(Date):
    startDateValue = RelationshipFrom(
        "Interval", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
    endDateValue = RelationshipFrom(
        "Interval", "xsdDateTime", cardinality=One, model=xsdDateTime
    )
