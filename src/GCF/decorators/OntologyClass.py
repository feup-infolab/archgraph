import importlib
import json

from marshmallow_jsonschema import JSONSchema


def decorator_schema(cls):
    def getSchema(self):
        json_schema = JSONSchema()
        return json_schema.dump(self)
    setattr(cls, 'getSchema', getSchema)

    def generate_template(self):
        schema = self.getSchema()
        class_name = self.__class__.__name__.split("Schema")[0]
        #todo arranjar isto
        #classes_name = self.get_superclasses_name()
        classes_name = [class_name]

        schema_class_name = class_name + "Schema"
        properties_of_entity = schema["definitions"][schema_class_name]["properties"]

        template_aux = {class_name: {}}
        template = {
            "classes_name": classes_name,
            "template": template_aux,
            "schema": json.dumps(schema)
        }
        for property_name in properties_of_entity:
            property = properties_of_entity[property_name]
            if property["type"] == "string":
                continue

            range = ""
            title = ""
            if property["type"] == "array":
                range = property["items"]["$ref"]
                title = property["title"]
            elif property["type"] == "object":
                title = property_name
                range = property["$ref"]

            range_schema_class_name = range.split("/")[2]
            range_class_name = range_schema_class_name.split("Schema")[0]
            template_aux[class_name][title] = range_class_name

        return template

    setattr(cls, 'generate_template', generate_template)

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

    # setattr(cls, "encodeJSON", encodeJSON)

    return cls
