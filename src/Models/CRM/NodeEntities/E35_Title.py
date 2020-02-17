from neomodel import (
    config,
    StructuredNode,
    StringProperty,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    DateTimeProperty,
    RelationshipFrom,
)
from NodeEntities.E33_Linguistic_Object import E33_Linguistic_Object
from NodeEntities.E71_Man_Made_Thing import E71_Man_Made_Thing
from src.Models.CRM.NodeProperties.StructuredRelCl import StructuredRelCl


class P102_has_title(StructuredRelCl):
    pass


class E35_Title(E33_Linguistic_Object):
    has_title = RelationshipFrom(
        E71_Man_Made_Thing, "P102_has_title", model=P102_has_title
    )
