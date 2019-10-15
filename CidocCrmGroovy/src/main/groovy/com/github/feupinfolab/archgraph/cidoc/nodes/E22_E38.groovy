package com.github.feupinfolab.archgraph.cidoc.nodes


import com.github.eugene.kamenev.orient.graph.Vertex
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E22_ManMade_Object_T
import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E38_Image_T
import groovy.transform.CompileStatic;


@CompileStatic
@Vertex(initSchema = true)
class E22_E38 implements E22_ManMade_Object_T, E38_Image_T{

}
