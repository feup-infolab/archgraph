from neomodel import RelationshipFrom

from NodeEntities.E77_Persistent_Item import E77_Persistent_Item
from NodeEntities.StructuredRelCl import StructuredRelCl


class P11_had_participant(StructuredRelCl):
    pass


class P14_carried_out_by(StructuredRelCl):
    pass


class E39_Actor(E77_Persistent_Item):
    had_participant = RelationshipFrom('E5_Event', 'P11_had_participant', model=P11_had_participant)
    carried_out_by = RelationshipFrom('E7_Activity','P14_carried_out_by', model=P14_carried_out_by)

