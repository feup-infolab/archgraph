package com.github.feupinfolab.archgraph.cidoc.edges


import com.github.eugene.kamenev.orient.graph.Edge
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E1_CRM_Entity_T
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E55_Type_T
import groovy.transform.CompileStatic

@Edge(from = E1_CRM_Entity_T, to = E55_Type_T)
@CompileStatic
class AP12_has_level_of_description {

}
