package com.github.feupinfolab.archgraph.cidoc.edges


import com.github.eugene.kamenev.orient.graph.Edge
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E1_CRM_Entity_T
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E41_Appellation_T
import groovy.transform.CompileStatic

@Edge(from = E1_CRM_Entity_T, to = E41_Appellation_T, initSchema = true)
@CompileStatic
class P1_is_identified_by {
    public Date since
}
