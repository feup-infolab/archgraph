package com.github.feupinfolab.archgraph.cidoc.nodes


import com.github.eugene.kamenev.orient.graph.Vertex
import com.github.feupinfolab.archgraph.cidoc.edges.P2_has_type
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E22_ManMade_Object_T
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E33_Linguistic_Object_T
import groovy.transform.CompileStatic;


@CompileStatic
@Vertex
class E22_E33 implements E22_ManMade_Object_T, E33_Linguistic_Object_T{
}
