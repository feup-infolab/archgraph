package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait PC102_has_title extends PC0_CRM_Property_T {

    @Relationship(type = "P102_1_has_type")
    E55_Type_T P102d1_has_type

    E55_Type_T getP102d1_has_type(){
        return P102d1_has_type
    }

    void setP102d1_has_type(E55_Type_T e55){
        P102d1_has_type = e55
    }

    static Object P102d1_has_type_t = E55_Type_T.class



}