package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship


@CompileStatic
trait E52_Time_Span_T implements E1_CRM_Entity_T{

    @Relationship(type = "P86_falls_within")
    private ArrayList<E52_Time_Span_T> P86_falls_within = new ArrayList<>()

    ArrayList<E52_Time_Span_T> getP86(){
        return P86_falls_within
    }

    @Relationship(type="AP14_has_date")
    Xsd_String AP14_has_date

    Xsd_String getAP14(){
        return AP14_has_date
    }

    void setAP14(Xsd_String ap14){
        AP14_has_date = ap14
    }

    @Relationship(type="AP15_has_date_of_description")
    Xsd_String AP15_has_date_of_description

    Xsd_String getAP15(){
        return AP15_has_date_of_description
    }

    void setAP15(Xsd_String ap15){
        AP15_has_date_of_description = ap15
    }

    @Relationship(type="AP16_has_production_date")
    Xsd_String AP16_has_production_date

    Xsd_String getAP16(){
        return AP16_has_production_date
    }

    void setAP16(Xsd_String ap16){
        AP16_has_production_date = ap16
    }

    @Relationship(type="AP17_has_last_modification")
    Xsd_String AP17_has_last_modification

    Xsd_String getAP17(){
        return AP17_has_last_modification
    }

    void setAP17(Xsd_String ap17){
        AP17_has_last_modification = ap17
    }





}