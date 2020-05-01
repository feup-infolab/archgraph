import datetime
import json
from marshmallow_jsonschema import JSONSchema

class SuperClass:
    def __init__(self, schema):
        self.schema = schema

    def getSchema(self):
        json_schema = JSONSchema()
        return json_schema.dump(self.schema)

    # Json to string
    def encodeJSON(self):
        data = {}
        for key, val in self.__properties__.items():
            if (key != "schema") and (key != "id"):
                data[key] = val

        def my_converter(o):
            if isinstance(o, datetime.datetime):
                return o.strftime("%Y-%m-%d")

        return json.dumps(data, default=my_converter)

    # string to json
    def decodeJSON(self):
        return json.loads(self.encodeJSON())

    def get_property_from_entity(self, property_name):
        schema_node = self.getSchema()
        class_name = self.__class__.__name__ + "Schema"
        return schema_node['definitions'][class_name]['properties'][property_name]

    def get_superclasses_name(self):
        return list(set(self.labels()))

    def get_schema_with_template(self, template):
        jsonSchema = self.getSchema()
        newJsonSchema = {
            '$schema': jsonSchema["$schema"],
            'definitions': {},
            '$ref': jsonSchema["$ref"],
        }
        self.__get_schema_with_template_aux(jsonSchema["definitions"], template, newJsonSchema)
        return newJsonSchema

    def __get_schema_with_template_aux(self, definitions, json_template, new_json_schema):
        if isinstance(json_template, str):
            entity_name = json_template
        else:
            entity_name = list(json_template.keys())[0]
        current_entity = entity_name + "Schema"
        entity = {}
        get_entity = new_json_schema["definitions"].get(current_entity, None)
        if  get_entity is not None:
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



        # array_uid = read_relationships(node_name, relationship_name)
        #
        # for uid in array_uid:
        #     node = get_node_by_uid(uid)

        return True

    def node_self_build(self, updated_node):
        object = {'self_node':{},
                  'relationships':{}}
        for property in updated_node.keys():
            if isinstance(updated_node[property], str):
                object['self_node'][property] = updated_node[property]
            elif isinstance(updated_node[property], dict):
                object['relationships'][property].apend(updated_node[property])
            elif isinstance(updated_node[property], list):
                relationships = []
                for element in updated_node[property]:
                    relationships.append(element)
                object['relationships'][property] = relationships
        return object

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


var = {'P1_is_identified_by': {'type': 'object',
                               '$ref': '#/definitions/E55_TypeSchema'},
       'P2_has_type': {'title': 'P2_has_type',
                       'type': 'array',
                       'items': {
                           'type': 'object',
                           '$ref': '#/definitions/E55_TypeSchema'}}}

var3 = {'P48_has_preferred_identifier': {
    'type': 'object',
    '$ref': '#/definitions/E42_IdentifierSchema'}, }

var1 = {'DataObjectSchema': {'properties': {
    'name': {'title': 'name',
             'type': 'string'},
    'uid': {'title': 'uid',
            'type': 'string'}},
    'type': 'object',
    'required': ['name'],
    'additionalProperties': False}}

var2 = {
    "E18_Physical_Thing": [
        {"P46_is_composed_of": "E18_Physical_Thing"}
    ]
}

var = {'$schema': 'http://json-schema.org/draft-07/schema#', 'definitions': {
    'E24_Physical_Human_Made_ThingSchema': {
        'type': 'object', 'properties': {
            'P130_shows_features_of': {
                'title': 'P130_shows_features_of',
                'type': 'array',
                'items': {'type': 'object',
                          '$ref': '#/definitions/E70_ThingSchema'}},
            'P62_depicts': {
                'title': 'P62_depicts',
                'type': 'array',
                'items': {'type': 'object',
                          '$ref': '#/definitions/E1_CRM_EntitySchema'}}},
        'additionalProperties': False},
    'E18_Physical_ThingSchema': {
        'type': 'object', 'properties': {
            'P46_is_composed_of': {
                'title': 'P46_is_composed_of',
                'type': 'array',
                'items': {'type': 'object',
                          '$ref': '#/definitions/E18_Physical_ThingSchema'}},
            'P59_has_section': {
                'title': 'P59_has_section',
                'type': 'array',
                'items': {'type': 'object',
                          '$ref': '#/definitions/E53_PlaceSchema'}}},
        'additionalProperties': False}},
       '$ref': '#/definitions/E18_Physical_ThingSchema'}
