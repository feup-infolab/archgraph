package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic

@Vertex(initSchema = true)
@CompileStatic
trait E2_Temporal_Entity_T implements E1_CRM_Entity_T{



    private ArrayList<E52_Time_Span_T> P4_has_time_span = new ArrayList<>()


    ArrayList<E52_Time_Span_T> getP4_has_time_span() {
        return P4_has_time_span
    }

    static Object P4_has_time_span_t = E52_Time_Span_T.class

}