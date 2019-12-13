package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait PC14_Carried_Out_By_T extends PC0_CRM_Property_T{

    @Relationship(type = "P14.1_in_the_role_of")
    E55_Type_T P14d1_in_the_role_of

    E55_Type_T getP14d1_in_the_role_of(){
        return P14d1_in_the_role_of
    }

    void setP14d1_in_the_role_of(E55_Type_T e55){
        P14d1_in_the_role_of = e55
    }

    static Object P14d1_in_the_role_of_t = E55_Type_T.class




}