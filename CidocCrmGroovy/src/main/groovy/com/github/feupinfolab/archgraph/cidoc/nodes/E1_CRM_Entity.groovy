package com.github.feupinfolab.archgraph.cidoc.nodes

import com.github.eugene.kamenev.orient.graph.Vertex
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E1_CRM_Entity_T
import groovy.transform.CompileStatic
import lombok.Getter
import lombok.Setter

@CompileStatic
@Vertex(initSchema = true)
@Getter
@Setter
class E1_CRM_Entity implements E1_CRM_Entity_T{
}
