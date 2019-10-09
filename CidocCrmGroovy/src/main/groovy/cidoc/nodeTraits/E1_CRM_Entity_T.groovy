package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic
import lombok.Getter

@Vertex
@CompileStatic
trait E1_CRM_Entity_T {
    @Getter
    private ArrayList<E41_Appellation_T> P1_is_identified_by = new ArrayList<>()
    @Getter
    private ArrayList<E55_Type_T> P2_has_type = new ArrayList<>()
    @Getter
    private ArrayList<E55_Type_T> AP12_has_level_of_description = new ArrayList<>()

    Xsd_String P3_has_note

    static mapping = {
        P1_is_identified_by(edge: E41_Appellation_T)
        P2_has_type(edge: E55_Type_T)
        AP12_has_level_of_description(edge: E55_Type_T)
    }
}