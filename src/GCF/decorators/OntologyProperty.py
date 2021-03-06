import importlib


def ontology_property(cls):

    # package_name = ".".join([cls.__module__, cls.__name__])
    package_name = ".".join(str.split(cls.__module__, ".")[:-2])
    module = importlib.import_module(package_name)

    # inject the base_uri, version and complete_uri from the GCF ontology
    # package
    setattr(cls, "base_uri", module.base_uri)
    setattr(cls, "version", module.version)
    setattr(cls, "full_uri", module.full_uri)

    def to_json(self):
        return {
            self.__class__.__name__: {
                "id": self.id,
                "start_node": self.start_node().__properties__,
                "end_node": self.end_node().__properties__,
            }
        }

    setattr(cls, "to_json", to_json)

    return cls
