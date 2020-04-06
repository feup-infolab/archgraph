import datetime
import importlib
import json


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
    # def encodeJSON(self):
    #     # return {self.__class__.__name__: self.__properties__}
    #     ___class = {}
    #     data = {}
    #     for key, val in self.__properties__.items():
    #         if (key != "schema") and (key != "id"):
    #             data[key] = val
    #     ___class[self.__class__.__name__] = data
    #
    #     def my_converter(o):
    #         if isinstance(o, datetime.datetime):
    #             return o.strftime("%Y-%m-%d")
    #
    #     return json.dumps(___class, default=my_converter)

    #setattr(cls, "encodeJSON", encodeJSON)

    return cls
