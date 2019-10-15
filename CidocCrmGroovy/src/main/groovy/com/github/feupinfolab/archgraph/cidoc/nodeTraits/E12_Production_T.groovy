package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic


@CompileStatic @Vertex(initSchema = true)
trait E12_Production_T implements E11_Modification_T, E63_Beginning_of_Existence_T{


    ArrayList<E24_Physical_ManMade_Thing_T> P108_has_produced = new ArrayList<>()

    ArrayList<E24_Physical_ManMade_Thing_T> getP108_has_produced(){
        return P108_has_produced
    }

    static Object P108_has_produced_t = E24_Physical_ManMade_Thing_T.class


}
