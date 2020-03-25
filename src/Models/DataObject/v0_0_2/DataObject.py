import datetime
from marshmallow import Schema, fields
from neomodel import StringProperty, StructuredNode, UniqueIdProperty
from src.Models.DataObject.v0_0_2.SuperClass import SuperClass


class Schema(Schema):
    uid = fields.String()
    name = fields.String(required=True)


class DataObject(StructuredNode, SuperClass):
    name = StringProperty(unique_index=True, required=True)
    uid = UniqueIdProperty()

    def __init__(self, schema=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if schema is None:
            schema = Schema()

        SuperClass.__init__(self, schema)

    def merge_node(self, updated_node):
        merged_node = dict(self.decodeJSON(), **updated_node)
        field_type_date = self.__get_field_of_type_date()

        for attr, value in merged_node.items():
            get_attr = getattr(self, attr)
            if get_attr != value:
                if attr in field_type_date:
                    value = datetime.datetime.strptime(value, '%Y-%m-%d')
                setattr(self, attr, value)
        try:
            self.save()
        except:
            return None
        return True

    # private method
    def __get_field_of_type_date(self):
        result = []
        get_schema = self.getSchema()
        properties = get_schema['definitions']['Schema']['properties']
        for attr in properties:
            field = properties[attr]
            if 'format' in field:
                result.append(field['title'])
        return result
