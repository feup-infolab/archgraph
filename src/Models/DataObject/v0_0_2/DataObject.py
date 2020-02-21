from neomodel import (IntegerProperty, RelationshipFrom, RelationshipTo,
                      StringProperty, StructuredNode, UniqueIdProperty, config)


class DataObject(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
