from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, One)
from json import JSONEncoder

from NodeProperties.StructuredRelCl import StructuredRelCl


class TestCardinality(StructuredRelCl):
    pass





class E1_CRM_Entity(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    testCardinality = RelationshipTo('E1_CRM_Entity', 'Cardinality_Relationship', cardinality=One,
                                     model=TestCardinality)

    def to_json(self):
        return {
            self.__class__.__name__: self.__properties__

        }
