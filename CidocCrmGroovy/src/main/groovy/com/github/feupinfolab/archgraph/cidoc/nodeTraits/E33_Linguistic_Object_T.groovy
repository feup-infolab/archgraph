package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic
import lombok.Getter
import lombok.Setter


@CompileStatic @Vertex(initSchema = true)
@Getter
@Setter
trait E33_Linguistic_Object_T implements E73_Information_Object_T{


    ArrayList<E56_Language_T> P72_has_language = new ArrayList<>()
    static Object P72_has_language_t = E56_Language_T.class
}