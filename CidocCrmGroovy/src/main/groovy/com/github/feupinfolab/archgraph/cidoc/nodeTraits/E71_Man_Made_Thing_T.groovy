package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic
import lombok.Getter
import lombok.Setter


@CompileStatic @Vertex(initSchema = true)
@Getter
@Setter
trait E71_Man_Made_Thing_T implements E70_Thing_T{
    ArrayList<E35_Title_T> P102_has_title= new ArrayList<>()
}