package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E22_ManMade_Object_T implements E19_Physical_Object_T, E24_Physical_ManMade_Thing_T{

    @Relationship(type="AP1_has_administrative_history")
    Xsd_String AP1_has_administrative_history

    Xsd_String getAP1(){
        return AP1_has_administrative_history
    }

    void setAP1(Xsd_String Ap1){
        AP1_has_administrative_history  = Ap1
    }


    @Relationship(type="AP2_has_archival_history")
    Xsd_String AP2_has_archival_history

    Xsd_String getAP2(){
        return AP2_has_archival_history
    }

    void setAP2(Xsd_String Ap2){
        AP2_has_archival_history  = Ap2
    }

    @Relationship(type="AP3_has_scope")
    Xsd_String AP3_has_scope

    Xsd_String getAP3(){
        return AP3_has_scope
    }

    void setAP3(Xsd_String Ap3){
        AP3_has_scope = Ap3
    }

    @Relationship(type="AP4_has_access_conditions")
    Xsd_String AP4_has_access_conditions

    Xsd_String getAP4(){
        return AP4_has_access_conditions
    }

    void setAP4(Xsd_String Ap4){
        AP4_has_access_conditions = Ap4
    }


    @Relationship(type="AP5_has_copies")
    Xsd_String AP5_has_copies

    Xsd_String getAP5(){
        return AP5_has_copies
    }

    void setAP5(Xsd_String Ap5){
        AP5_has_copies = Ap5
    }

    @Relationship(type="AP6_has_publication_note")
    Xsd_String AP6_has_publication_note

    Xsd_String getAP6(){
        return AP6_has_publication_note
    }

    void setAP6(Xsd_String Ap6){
        AP6_has_publication_note = Ap6
    }

    @Relationship(type="AP7_has_publication_note")
    Xsd_String AP7_has_publication_note

    Xsd_String getAP7(){
        return AP7_has_publication_note
    }

    void setAP7(Xsd_String Ap7){
        AP7_has_publication_note = Ap7
    }





}