package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_Date
import cidoc.nodeEntities.Xsd_Date
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship


@CompileStatic
trait E52_Time_Span_T implements E1_CRM_Entity_T{

    @Relationship(type = "P86_falls_within")
    private ArrayList<E52_Time_Span_T> P86_falls_within = new ArrayList<>()

    ArrayList<E52_Time_Span_T> getP86_falls_within(){
        return P86_falls_within
    }

    static Object P86_falls_within_t = E52_Time_Span_T.class


    @Relationship(type="AP14_has_date")
    Xsd_Date AP14_has_date

    Xsd_Date getAP14_has_date(){
        return AP14_has_date
    }

    void setAP14_has_date(Xsd_Date ap14){
        AP14_has_date = ap14
    }

    @Relationship(type="AP15_has_date_of_description")
    Xsd_Date AP15_has_date_of_description

    Xsd_Date getAP15_has_date_of_description(){
        return AP15_has_date_of_description
    }

    void setAP15_has_date_of_description(Xsd_Date ap15){
        AP15_has_date_of_description = ap15
    }

    @Relationship(type="AP16_has_production_date")
    Xsd_Date AP16_has_production_date

    Xsd_Date getAP16_has_production_date(){
        return AP16_has_production_date
    }

    void setAP16_has_production_date(Xsd_Date ap16){
        AP16_has_production_date = ap16
    }

    @Relationship(type="AP17_has_last_modification")
    Xsd_Date AP17_has_last_modification

    Xsd_Date getAP17_has_last_modification(){
        return AP17_has_last_modification
    }

    void setAP17_has_last_modification(Xsd_Date ap17){
        AP17_has_last_modification = ap17
    }





}