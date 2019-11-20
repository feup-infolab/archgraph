package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.NodeEntity
import org.neo4j.ogm.annotation.Relationship

import javax.management.relation.Relation

@CompileStatic
trait E1_CRM_Entity_T {


    static Object P1_is_identified_by_t = E41_Appellation_T.class

    @Relationship(type="P1_is_identified_by")
    private ArrayList<E41_Appellation_T> P1_is_identified_by = new ArrayList<>()

    ArrayList<E41_Appellation_T> getP1_is_identified_by(){
        return P1_is_identified_by
    }

    static Object P2_has_type_t = E55_Type_T.class

    @Relationship(type="P2_has_type")
    private ArrayList<E55_Type_T> P2_has_type = new ArrayList<>()

    ArrayList<E55_Type_T> getP2_has_type(){
        return P2_has_type
    }

    //ArrayList<E55_Type_T> getP2_has_type(){
    //    return P2_has_type
    //}

    @Relationship(type="AP12_has_level_of_description")
    private ArrayList<E55_Type_T> AP12_has_level_of_description = new ArrayList<>()

    ArrayList<E55_Type_T> getAP12_has_level_of_description(){
        return AP12_has_level_of_description
    }
    static Object AP12_has_level_of_description_t = E55_Type_T.class

    @Relationship(type="P3_has_note")
    Xsd_String P3_has_note

    Xsd_String getP3_has_note(){
        return P3_has_note
    }

    void setP3_has_note(Xsd_String p3){
        P3_has_note = p3
    }




}