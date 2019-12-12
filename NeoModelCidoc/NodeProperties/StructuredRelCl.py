from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, StructuredRel)


class StructuredRelCl(StructuredRel):
    def to_json(self):
        return {
            self.__class__.__name__: {
                "id": self.id,
                "type": self.start_node().__class__.__name__,
                "start_node": self.start_node().__properties__,
                "end_node": self.end_node().__properties__
            }}
