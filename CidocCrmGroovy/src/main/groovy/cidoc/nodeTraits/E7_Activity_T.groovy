package cidoc.nodeTraits

import cidoc.nodeEntities.E55_Type
import org.neo4j.ogm.annotation.Relationship

trait E7_Activity_T implements E5_Event_T{

    @Relationship(type = "P21_had_general_purpose")
    ArrayList<E55_Type_T> P21_had_general_purpose = new ArrayList<>()

    ArrayList<E55_Type_T> getP21(){
        return P21_had_general_purpose
    }

    @Relationship(type = "P14_carried_out_by")
    ArrayList<E39_Actor_T> P14_carried_out_by = new ArrayList<>()

    ArrayList<E39_Actor_T> getP14(){
        return P14_carried_out_by
    }

    void p14_1(E39_Actor_T e39_actor_t,E55_Type_T e55_type_t){
        if(e39_actor_t.p14_1 == null){
        p14.add(e39_actor_t)
        e39_actor_t.p14_1 = e55_type_t}
    }


}