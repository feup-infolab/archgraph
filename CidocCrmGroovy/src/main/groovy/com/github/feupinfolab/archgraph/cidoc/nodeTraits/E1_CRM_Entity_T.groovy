package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import com.github.feupinfolab.archgraph.cidoc.edges.AP12_has_level_of_description
import com.github.feupinfolab.archgraph.cidoc.edges.P1_is_identified_by
import com.github.feupinfolab.archgraph.cidoc.edges.P2_has_type
import com.github.feupinfolab.archgraph.dataobject.Xsd_String
import groovy.transform.CompileDynamic
import groovy.transform.CompileStatic
import groovy.transform.TypeChecked
import groovy.transform.TypeCheckingMode
import lombok.AccessLevel
import lombok.Getter
import lombok.Setter

@Vertex(initSchema = true)
@CompileStatic
@Getter
@Setter
trait E1_CRM_Entity_T {
    String name

    List<E41_Appellation_T> isIdentifiedBy
    List<E55_Type_T> hasType
    List<E55_Type_T> hasLevelOfDescription

    Xsd_String P3_has_note

    @Getter(AccessLevel.NONE)
    @Setter(AccessLevel.NONE)

    static mapping = {
        hasType edge: P2_has_type
        isIdentifiedBy edge: P1_is_identified_by
        hasLevelOfDescription edge: AP12_has_level_of_description
    }
}