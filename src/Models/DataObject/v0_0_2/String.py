from neomodel import One, RelationshipFrom, StructuredRel

from .DataObject import DataObject


class xsdString(StructuredRel):
    pass


class String(DataObject):
    stringValue = RelationshipFrom(
        "String", "xsdString", cardinality=One, model=xsdString
    )
