import json

from marshmallow import Schema, fields
from neomodel import StringProperty
from src.Models.DataObject.v0_0_2.DataObject import DataObject
from src.Models.DataObject.v0_0_2.SerializeClass import SerializeClass


class StringSchema(Schema):
    stringValue = fields.String(required=True)


# class String(DataObject):
#     stringValue = StringProperty(unique_index=True, required=True)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.list.append(self.stringValue)

class String(DataObject):
    stringValue = StringProperty(unique_index=True, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(StringSchema(), *args, **kwargs)
        self.list.append(self.stringValue)


