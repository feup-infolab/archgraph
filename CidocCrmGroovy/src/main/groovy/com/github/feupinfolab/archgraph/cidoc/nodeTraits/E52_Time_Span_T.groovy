package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.feupinfolab.archgraph.dataobject.Xsd_Date
import groovy.transform.CompileStatic
import com.github.eugene.kamenev.orient.graph.Vertex

@CompileStatic @Vertex(initSchema = true)
trait E52_Time_Span_T implements E1_CRM_Entity_T{

    
    private ArrayList<E52_Time_Span_T> P86_falls_within = new ArrayList<>()

    ArrayList<E52_Time_Span_T> getP86_falls_within(){
        return P86_falls_within
    }

    static Object P86_falls_within_t = E52_Time_Span_T.class


    Xsd_Date AP14_has_date

    Xsd_Date getAP14_has_date(){
        return AP14_has_date
    }

    void setAP14_has_date(Xsd_Date ap14){
        AP14_has_date = ap14
    }

    
    Xsd_Date AP15_has_date_of_description

    Xsd_Date getAP15_has_date_of_description(){
        return AP15_has_date_of_description
    }

    void setAP15_has_date_of_description(Xsd_Date ap15){
        AP15_has_date_of_description = ap15
    }

    
    Xsd_Date AP16_has_production_date

    Xsd_Date getAP16_has_production_date(){
        return AP16_has_production_date
    }

    void setAP16_has_production_date(Xsd_Date ap16){
        AP16_has_production_date = ap16
    }

    
    Xsd_Date AP17_has_last_modification

    Xsd_Date getAP17_has_last_modification(){
        return AP17_has_last_modification
    }

    void setAP17_has_last_modification(Xsd_Date ap17){
        AP17_has_last_modification = ap17
    }





}