package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic


@CompileStatic @Vertex(initSchema = true)
trait E90_Symbolic_Object_T implements E72_Legal_Object_T, E28_Conceptual_Object_T {

    
    ArrayList<E90_Symbolic_Object_T> P106_is_composed_of = new ArrayList<>()

    ArrayList<E90_Symbolic_Object_T> getP106_is_composed_of(){
        return P106_is_composed_of
    }

    static Object P106_is_composed_of_t = E90_Symbolic_Object_T.class


}
