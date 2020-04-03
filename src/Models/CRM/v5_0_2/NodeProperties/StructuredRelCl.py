import json

from neomodel import StructuredRel


class StructuredRelCl(StructuredRel):
    # Json to string
    def encodeJSON(self):
        return {
            self.__class__.__name__: {
                # "id": self.id,
                # "start_node": json.loads(self.start_node().encodeJSON()),
                "end_node": json.loads(self.end_node().encodeJSON()),
            }
        }
