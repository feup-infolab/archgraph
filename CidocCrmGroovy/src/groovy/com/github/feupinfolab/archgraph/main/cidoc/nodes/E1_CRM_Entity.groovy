package cidoc.nodes

import cidoc.nodeTraits.E1_CRM_Entity_T
import cidoc.nodeTraits.E41_Appellation_T
import cidoc.nodeTraits.E55_Type_T
import com.github.eugene.kamenev.orient.graph.Vertex
import dataobject.Xsd_String
import groovy.transform.CompileStatic
import lombok.Getter;


@CompileStatic
@Vertex
class E1_CRM_Entity implements E1_CRM_Entity_T{
    @Getter
    private ArrayList<E41_Appellation_T> P1_is_identified_by = new ArrayList<>()
    @Getter
    private ArrayList<E55_Type_T> P2_has_type = new ArrayList<>()
    @Getter
    private ArrayList<E55_Type_T> AP12_has_level_of_description = new ArrayList<>()

    Xsd_String P3_has_note

    static mapping = {
        P1_is_identified_by(edge: P1_is_identified_by)
        // P2_has_type(edge: E55_Type_T)
        // AP12_has_level_of_description(edge: E55_Type_T)
    }
}
