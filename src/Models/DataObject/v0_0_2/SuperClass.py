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
        first_entity = list(jsonTemplate.keys())[0]
        self.get_schema_with_template_aux(jsonSchema["definitions"][first_entity + "Schema"], jsonTemplate)

        return

        {"E70_Thing": [
            {
                "P130_shows_features_of": {
                    "E24_Physical_Human_Made_Thing": [
                        {"P102_has_title": "E35_Title"},
                        {"P156_occupies": "E53_Place"},
                    ]
                }
            }
        ]
        }

    def get_schema_with_template_aux(self, entitySchema, entity_json):
        if isinstance(entity_json, str):
            return

        entity_name = list(entity_json.keys())[0]
        entity = {
            entity_name: {
                'properties': {}
            }
        }
        properties = entitySchema['properties']

        for property_entity in entity_json[entity_name]:

            property_name = list(property_entity.keys())[0]
            next_property = property_entity[property_name]

            self.get_schema_with_template_aux(entitySchema, next_property)

        return entity


# {'title': 'name', 'type': 'string'}
{'$schema': 'http://json-schema.org/draft-07/schema#', 'definitions': {'E36_Visual_ItemSchema':
                                                                           {'properties': {'P65_shows_visual_item':
                                                                                               {
                                                                                                   'title': 'P65_shows_visual_item',
                                                                                                   'type': 'array',
                                                                                                   'items':
                                                                                                       {
                                                                                                           'type': 'object',
                                                                                                           '$ref': '#/definitions/E24_Physical_Human_Made_ThingSchema'}}},
                                                                            'type': 'object',
                                                                            'additionalProperties': False},
                                                                       'E24_Physical_Human_Made_ThingSchema': {
                                                                           'properties': {'P108_has_produced_by': {
                                                                               'title': 'P108_has_produced_by',
                                                                               'type': 'array',
                                                                               'items': {'type': 'object',
                                                                                         '$ref': '#/definitions/E1_CRM_EntitySchema'}},
                                                                                          'P62_depicts': {
                                                                                              'title': 'P62_depicts',
                                                                                              'type': 'array',
                                                                                              'items': {
                                                                                                  'type': 'object',
                                                                                                  '$ref': '#/definitions/E1_CRM_EntitySchema'}}},
                                                                           'type': 'object',
                                                                           'additionalProperties': False},
                                                                       'E1_CRM_EntitySchema': {'properties': {
                                                                           'P138_represents': {
                                                                               'title': 'P138_represents',
                                                                               'type': 'array',
                                                                               'items': {'type': 'object',
                                                                                         '$ref': '#/definitions/E36_Visual_ItemSchema'}},
                                                                           'has_value': {'title': 'has_value',
                                                                                         'type': 'array',
                                                                                         'items': {'type': 'object',
                                                                                                   '$ref': '#/definitions/DataObjectSchema'}},
                                                                           'name': {'title': 'name', 'type': 'string'},
                                                                           'uid': {'title': 'uid', 'type': 'string'}},
                                                                                               'type': 'object',
                                                                                               'required': ['name'],
                                                                                               'additionalProperties': False},
                                                                       'DataObjectSchema': {'properties': {
                                                                           'name': {'title': 'name', 'type': 'string'},
                                                                           'uid': {'title': 'uid', 'type': 'string'}},
                                                                                            'type': 'object',
                                                                                            'required': ['name'],
                                                                                            'additionalProperties': False}},
 '$ref': '#/definitions/E1_CRM_EntitySchema'}
