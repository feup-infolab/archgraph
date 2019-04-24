package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait PC14_Carried_Out_By_T extends PC0_CRM_Property_T{

    @Relationship(type = "P14_1_in_the_role_of")
    E55_Type_T P14_1_in_the_role_of

    E55_Type_T getP14_1(){
        return P14_1_in_the_role_of
    }

    void setP14_1(E55_Type_T e55){
        P14_1_in_the_role_of = e55
    }

}