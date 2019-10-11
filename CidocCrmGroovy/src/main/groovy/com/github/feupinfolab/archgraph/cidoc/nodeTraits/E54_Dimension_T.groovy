package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.feupinfolab.archgraph.dataobject.Xsd_Integer


trait E54_Dimension_T implements E1_CRM_Entity_T{

    
    Xsd_Integer P90_has_value

    Xsd_Integer getP90_has_value(){
        return P90_has_value
    }

    void setP90_has_value(Xsd_Integer P90){
        P90_has_value  = P90
    }




}