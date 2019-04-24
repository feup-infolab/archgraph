package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait PC14_Carried_Out_By_T extends PC0_CRM_Property_T{

    @Relationship(type = "P14.1_in_the_role_of")
    E55_Type_T P14d1_in_the_role_of

    E55_Type_T getP14d1(){
        return P14d1_in_the_role_of
    }

    void setP14d1(E55_Type_T e55){
        P14d1_in_the_role_of = e55
    }




}