from abc import ABC

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


class E28_Conceptual_Object(StructuredNode):
    conProp = StringProperty(unique_index=True, required=True)


class E55_Type(E28_Conceptual_Object):
    typeName = StringProperty(unique_index=True, required=True)


class E56_Language(E55_Type):
    languageName = StringProperty(unique_index=True, required=True)


class E1_CRM_Entity(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    hasType = RelationshipTo(E55_Type, 'P2_has_type')


e1 = E1_CRM_Entity(name='E1_CRM test').save()  # Create
var = e1.id  # neo4j internal id
type1 = E55_Type(typeName='Type Example', conProp="Proof of Hierarchy").save()
conObj = E28_Conceptual_Object(conProp='Conceptual Object Property').save()
lan = E56_Language(typeName='Language Example', languageName='Language Example', conProp="Con Obj Proof").save()
e1.hasType.connect(type1)
e1.hasType.connect(lan)
e1.hasType.connect(conObj)
