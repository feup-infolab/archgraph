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
            'definitions': {}
        }
        self.get_schema_with_template_aux(jsonSchema["definitions"], jsonTemplate, newJsonSchema)
        print(newJsonSchema)
        print(jsonSchema)

        return newJsonSchema

    def get_schema_with_template_aux(self, definitions, json_template, newJsonSchema):
        if isinstance(json_template, str):
            return

        entity_name = list(json_template.keys())[0]
        current_entity = entity_name + "Schema"
        entity = {
            current_entity: {
                'type': definitions[current_entity]['type'],
                'properties': {},
                'additionalProperties': definitions[current_entity]['additionalProperties'],
            }
        }
        if hasattr(definitions[current_entity], 'required'):
            entity[current_entity]['required'] = definitions[current_entity]['required']

        newJsonSchema['definitions'][entity_name] = entity

        properties = definitions[current_entity]['properties']

        for property_entity in json_template[entity_name]:
            property_name = list(property_entity.keys())[0]
            next_entity = property_entity[property_name]
            if isinstance(next_entity, str):
                new_property = definitions[current_entity]['properties'][property_name]

                changed_property = {
                    'type': new_property['type'],
                }
                if new_property['type'] == 'object' and hasattr(new_property, '$ref'):
                    changed_property['type'] = 'string'

                if new_property['type'] == 'array' and new_property['items']['type'] == 'object':
                    changed_property['items'] = {
                        'type': 'string'}
                    changed_property['title'] = new_property['title']

                entity[current_entity]['properties'][property_name] = changed_property

            else:
                entity[entity_name]['properties'][property_name] = properties[property_name]

            self.get_schema_with_template_aux(definitions, next_entity, newJsonSchema)


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
