from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, StructuredRel)


class StructuredRelCl(StructuredRel):
    def to_json(self):
        return {
            "id": self.id,
            "start_node": self.start_node(),
            "end_node": self.end_node()
        }
