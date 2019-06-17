package cidoc.nodeTraits

import cidoc.nodeEntities.E1_Crm_Entity
import cidoc.nodeEntities.E55_Type
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E7_Activity_T implements E5_Event_T{

    @Relationship(type = "P21_had_general_purpose")
    ArrayList<E55_Type_T> P21_had_general_purpose = new ArrayList<>()

    ArrayList<E55_Type_T> getP21_had_general_purpose(){
        return P21_had_general_purpose
    }

    static Object P21_had_general_purpose_t = E55_Type_T.class

    @Relationship(type = "P14_carried_out_by")
    ArrayList<E39_Actor_T> P14_carried_out_by = new ArrayList<>()

    ArrayList<E39_Actor_T> getP14_carried_out_by(){
        return P14_carried_out_by
    }

    static Object P14_carried_out_by_t = E39_Actor_T.class

    @Relationship(type = "P15_was_influenced_by")
    ArrayList<E1_CRM_Entity_T> P15_was_influenced_by = new ArrayList<>()

    ArrayList<E1_CRM_Entity_T> getP15_was_influenced_by(){
        return P15_was_influenced_by
    }

    static Object P15_was_influenced_by_t = E1_CRM_Entity_T.class




}