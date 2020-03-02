import importlib
from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema
from functools import wraps # This convenience func preserves name and docstring

def has_json_schema(cls):

    def getSchema(self):
        string_schema = StringSchema()
        json_schema = JSONSchema()
        return json_schema.dump(string_schema)

    # package_name = ".".join([cls.__module__, cls.__name__])
    package_name = ".".join(str.split(cls.__module__, ".")[:-2])
    module = importlib.import_module(cls.__module__ + "Schema")



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
