import importlib
import json

from marshmallow_jsonschema import JSONSchema


def json_serializable(cls):
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    setattr(cls, "print_schema", toJSON)


def has_json_schema(cls):
    if not hasattr(cls, "get_schema"):
        raise Exception(
            "JSON-serializable Ontology classes must declare a static get_schema method"
        )

    def print_schema(self):
        json_schema = JSONSchema()
        class_schema = cls.__module__
        return json_schema.dump(class_schema)

    # # este código injeta métodos de instância numa classe
    # defaultInit = getattr(cls, '__init__')
    #
    # def newInit(self, *args, **kwargs):
    #     defaultInit(self, *args, **kwargs)
    #     setattr(self, "get_schema", get_schema)
    #     setattr(self, "print_schema", print_schema)
    #
    # setattr(cls, "__init__", newInit)

    setattr(cls, "print_schema", print_schema)

    return cls


def ontology_class(cls):

    # package_name = ".".join([cls.__module__, cls.__name__])
    package_name = ".".join(str.split(cls.__module__, ".")[:-2])
    module = importlib.import_module(package_name)

    # inject the base_uri, version and complete_uri from the GCF ontology
    # package
    setattr(cls, "base_uri", module.base_uri)
    setattr(cls, "version", module.version)
    setattr(cls, "full_uri", module.full_uri)

    # add default serializer
    def to_json(self):
        return {self.__class__.__name__: self.__properties__}

    setattr(cls, "to_json", to_json)

    return cls
