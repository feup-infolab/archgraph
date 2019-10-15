package com.github.feupinfolab.archgraph.cidoc.edges


import com.github.eugene.kamenev.orient.graph.Edge
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E1_CRM_Entity_T
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E55_Type_T
import com.github.feupinfolab.archgraph.cidoc.nodes.E55_Type
import groovy.transform.CompileStatic

@Edge(from = E1_CRM_Entity_T, to = E55_Type, initSchema = true)
@CompileStatic
class P2_has_type {

}
