package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import groovy.transform.CompileStatic


@CompileStatic
trait E53_Place_T implements E1_CRM_Entity_T{
    
    private ArrayList<E41_Appellation_T> P87_is_identified_by = new ArrayList<>()

    ArrayList<E41_Appellation_T> getP87_is_identified_by(){
        return P87_is_identified_by
    }

    static Object P87_is_identified_by_t = E41_Appellation_T.class


}