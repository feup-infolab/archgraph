package com.github.feupinfolab.archgraph.cidoc.nodeTraits

import com.github.feupinfolab.archgraph.dataobject.Xsd_String
import groovy.transform.CompileStatic
import lombok.Getter
import lombok.Setter


@CompileStatic
@Getter
@Setter
trait E22_ManMade_Object_T implements E19_Physical_Object_T, E24_Physical_ManMade_Thing_T {
    Xsd_String AP1_has_administrative_history
    Xsd_String AP2_has_archival_history
    Xsd_String AP3_has_scope
    Xsd_String AP4_has_access_conditions
    Xsd_String AP5_has_copies
    Xsd_String AP6_has_publication_note
    Xsd_String AP7_has_publication_note
}