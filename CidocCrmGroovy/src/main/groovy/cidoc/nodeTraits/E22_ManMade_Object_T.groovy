package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic


@CompileStatic
trait E22_ManMade_Object_T implements E19_Physical_Object_T,E24_Physical_ManMade_Thing_T{


    Xsd_String AP1_has_administrative_history

    Xsd_String getAP1_has_administrative_history(){
        return AP1_has_administrative_history
    }

    void setAP1_has_administrative_history(Xsd_String Ap1){
        AP1_has_administrative_history  = Ap1
    }



    Xsd_String AP2_has_archival_history

    Xsd_String getAP2_has_archival_history(){
        return AP2_has_archival_history
    }

    void setAP2_has_archival_history(Xsd_String Ap2){
        AP2_has_archival_history  = Ap2
    }


    Xsd_String AP3_has_scope

    Xsd_String getAP3_has_scope(){
        return AP3_has_scope
    }

    void setAP3_has_scope(Xsd_String Ap3){
        AP3_has_scope = Ap3
    }


    Xsd_String AP4_has_access_conditions

    Xsd_String getAP4_has_access_conditions(){
        return AP4_has_access_conditions
    }

    void setAP4_has_access_conditions(Xsd_String Ap4){
        AP4_has_access_conditions = Ap4
    }



    Xsd_String AP5_has_copies

    Xsd_String getAP5_has_copies(){
        return AP5_has_copies
    }

    void setAP5_has_copies(Xsd_String Ap5){
        AP5_has_copies = Ap5
    }


    Xsd_String AP6_has_publication_note

    Xsd_String getAP6_has_publication_note(){
        return AP6_has_publication_note
    }

    void setAP6_has_publication_note(Xsd_String Ap6){
        AP6_has_publication_note = Ap6
    }


    Xsd_String AP7_has_publication_note

    Xsd_String getAP7_has_publication_note(){
        return AP7_has_publication_note
    }

    void setAP7_has_publication_note(Xsd_String Ap7){
        AP7_has_publication_note = Ap7
    }





}