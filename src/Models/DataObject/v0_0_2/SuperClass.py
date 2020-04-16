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
        ___class = {}
        for key, val in self.__properties__.items():
            if (key != "schema") and (key != "id"):
                data[key] = val
            ___class[self.__class__.__name__] = data

        def my_converter(o):
            if isinstance(o, datetime.datetime):
                return o.strftime("%Y-%m-%d")

        return json.dumps(___class, default=my_converter)

    # string to json
    def decodeJSON(self):
        return json.loads(self.encodeJSON())

    def get_schema_with_template(self, jsonTemplate):
        jsonSchema = self.getSchema()
        newJsonSchema = {
            '$schema': jsonSchema["$schema"],
            'definitions': {},
            '$ref': jsonSchema["$ref"],
        }
        self.__get_schema_with_template_aux(jsonSchema["definitions"], jsonTemplate, newJsonSchema)
        print(newJsonSchema)
        print(jsonSchema)

        return newJsonSchema

    def __get_schema_with_template_aux(self, definitions, json_template, newJsonSchema):
        if isinstance(json_template, str):
            entity_name = json_template
        else:
            entity_name = list(json_template.keys())[0]
        current_entity = entity_name + "Schema"
        entity = {
                'type': definitions[current_entity]['type'],
                'properties': {},
                'additionalProperties': definitions[current_entity]['additionalProperties'],
        }
        if 'required' in definitions[current_entity].keys():
            entity['required'] = definitions[current_entity]['required']

        newJsonSchema['definitions'][current_entity] = entity

        properties = definitions[current_entity]['properties']

        self.__get_entity_properties_without_ref(definitions[current_entity], entity)

        if isinstance(json_template, str):
            return

        for property_entity in json_template[entity_name]:
            property_name = list(property_entity.keys())[0]
            next_entity = property_entity[property_name]

            entity['properties'][property_name] = properties[property_name]

            self.__get_schema_with_template_aux(definitions, next_entity, newJsonSchema)

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
