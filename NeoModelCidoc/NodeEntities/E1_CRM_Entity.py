from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One, RelationshipFrom)
from json import JSONEncoder

from NodeEntities.StructuredRelCl import StructuredRelCl


class P14_carried_out_by(StructuredRelCl):
    pass


class E1_CRM_Entity(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    carried_out_by = RelationshipFrom('E7_Activity', 'P14_carried_out_by',
                                     model=P14_carried_out_by)

    def to_json(self):
        return {
            self.__class__.__name__: self.__properties__

        }
