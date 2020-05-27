import datetime
import json
from marshmallow_jsonschema import JSONSchema


class SuperClass:
    def __init__(self, schema):
        self.schema = schema

    """The function returns the node schema"""
    def getSchema(self):
        json_schema = JSONSchema()
        return json_schema.dump(self.schema)

    """The function returns the node information in string"""
    def encodeJSON(self):
        data = {}
        for key, val in self.__properties__.items():
            if (key != "schema") and (key != "id"):
                data[key] = val

        def my_converter(o):
            if isinstance(o, datetime.datetime):
                return o.strftime("%Y-%m-%d")

        return json.dumps(data, default=my_converter)

    """The function returns the node information at format json"""
    def decodeJSON(self):
        return json.loads(self.encodeJSON())

    """The function returns the property of entity with name property_name"""
    def get_property_from_entity(self, property_name):
        schema_node = self.getSchema()
        class_name = self.__class__.__name__ + "Schema"
        return schema_node['definitions'][class_name]['properties'][property_name]

    """The function returns its superclasses names"""
    def get_superclasses_name(self):
        return list(set(self.labels()))

    """The function returns the schema according to the template provided"""
    def get_schema_with_template(self, template):
        jsonSchema = self.getSchema()
        newJsonSchema = {
            '$schema': jsonSchema["$schema"],
            'definitions': {},
            '$ref': jsonSchema["$ref"],
        }
        self.__get_schema_with_template_aux(jsonSchema["definitions"], template, newJsonSchema)
        return newJsonSchema

    """Auxiliary function - The function returns the schema according to the template provided"""
    def __get_schema_with_template_aux(self, definitions, json_template, new_json_schema):
        if isinstance(json_template, str):
            entity_name = json_template
        else:
            entity_name = list(json_template.keys())[0]
        current_entity = entity_name + "Schema"
        entity = {}
        get_entity = new_json_schema["definitions"].get(current_entity, None)
        if get_entity is not None:
            entity = new_json_schema["definitions"][current_entity]
        else:
            entity = {
                'type': definitions[current_entity]['type'],
                'properties': {},
                'additionalProperties': definitions[current_entity]['additionalProperties'],
            }
            if 'required' in definitions[current_entity].keys():
                entity['required'] = definitions[current_entity]['required']

            new_json_schema['definitions'][current_entity] = entity

        properties = definitions[current_entity]['properties']

        self.__get_entity_properties_without_ref(definitions[current_entity], entity)

        if isinstance(json_template, str):
            return

        for property_name in json_template[entity_name]:
            next_entity = json_template[entity_name][property_name]

            entity['properties'][property_name] = properties[property_name]

            self.__get_schema_with_template_aux(definitions, next_entity, new_json_schema)

    def __get_entity_properties_without_ref(self, current_entity, entity):
        for property_name in current_entity['properties']:
            property_entity = current_entity['properties'][property_name]

            if property_entity['type'] != 'object' and property_entity['type'] != 'array':
                entity['properties'][property_name] = property_entity

            #
            # if property_entity['type'] == 'object' and '$ref' in property_entity.keys():
            #     changed_property['type'] = 'string'
            #
            # if property_entity['type'] == 'array' and property_entity['items']['type'] == 'object':
            #     changed_property['items'] = {
            #         'type': 'string'}
            #     changed_property['title'] = property_entity['title']

    """The function merges between node and customer data, then saves the node"""
    def merge_node(self, updated_node):
        merged_node = dict(self.decodeJSON(), **updated_node)
        field_type_date = self.__get_field_of_type_date()

        for attr, value in merged_node.items():
            get_attr = getattr(self, attr)
            if get_attr != value:
                if attr in field_type_date:
                    value = datetime.datetime.strptime(value, "%Y-%m-%d")
                setattr(self, attr, value)
        try:
            self.save()
        except BaseException:
            return None
        return True

    """The function returns the node with updated fields and relationships"""
    def build_node(self, data):
        node = {'self_node': {},
                  'relationships': {}}
        for property in data.keys():
            if isinstance(data[property], str):
                node['self_node'][property] = data[property]
            elif isinstance(data[property], dict):
                node['relationships'][property] = []
                node['relationships'][property].append(data[property])
            elif isinstance(data[property], list):
                relationships = []
                for element in data[property]:
                    relationships.append(element)
                node['relationships'][property] = relationships
        return node

    """The function returns entity's fields of type date"""
    def __get_field_of_type_date(self):
        result = []
        get_schema = self.getSchema()
        class_name = self.__class__.__name__ + "Schema"
        properties = get_schema["definitions"][class_name]["properties"]
        for attr in properties:
            field = properties[attr]
            if "format" in field:
                result.append(field["title"])
        return result

