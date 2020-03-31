import datetime

from marshmallow import Schema, fields
from neomodel import StringProperty, StructuredNode, UniqueIdProperty
from src.Models.DataObject.v0_0_2.SuperClass import SuperClass


class DataObjectSchema(Schema):
    uid = fields.String()
    name = fields.String(required=True)


class DataObject(StructuredNode, SuperClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()

    def __init__(self, schema=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if schema is None:
            schema = DataObjectSchema()

        SuperClass.__init__(self, schema)

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

    # private method
    def __get_field_of_type_date(self):
        result = []
        get_schema = self.getSchema()
        properties = get_schema["definitions"]["Schema"]["properties"]
        for attr in properties:
            field = properties[attr]
            if "format" in field:
                result.append(field["title"])
        return result


var = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "definitions": {
        "PersonNameSchema": {
            "properties": {
                "name": {"title": "name", "type": "string"},
                "person_name": {"title": "person_name", "type": "string"},
                "stringValue": {"title": "stringValue", "type": "string"},
                "uid": {"title": "uid", "type": "string"},
            },
            "required": ["name", "person_name", "stringValue"],
            "type": "object",
            "additionalProperties": False,
        }
    },
    "$ref": "#/definitions/PersonNameSchema",
}
