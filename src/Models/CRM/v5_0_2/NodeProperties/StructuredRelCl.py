from neomodel import StructuredRel


class StructuredRelCl(StructuredRel):
    def to_json(self):
        a = self.start_node()
        return {
            self.__class__.__name__: {
                # "id": self.id,
                "start_node": self.start_node().to_json(),
                "end_node": self.end_node().to_json,
            }
        }
