from neomodel import One, RelationshipFrom, StructuredRel

from .String import String


class xsdString(StructuredRel):
    pass


class RegexString(String):
    hasRegex = RelationshipFrom(
        "RegexString", "xsdString", cardinality=One, model=xsdString
    )
