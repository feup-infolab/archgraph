package cidoc.nodeTraits

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


}