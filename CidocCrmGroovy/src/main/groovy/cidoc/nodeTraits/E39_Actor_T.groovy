package cidoc.nodeTraits

import cidoc.nodeEntities.E55_Type
import org.neo4j.ogm.annotation.Relationship

trait E39_Actor_T implements E77_Persistent_Item_T{


    @Relationship(type = "P14_1_in_the_role_of")
    E55_Type_T P14_1_in_the_role_of = null

    E55_Type_T getP14_1(){
        return P14_1_in_the_role_of
    }

    void setP14_1(E55_Type_T e55_type_t){
        if(e55_type_t.ternaryId == null){
        P14_1_in_the_role_of = e55_type_t}
    }
}