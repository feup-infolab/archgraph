package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic
import lombok.Getter

@Vertex
@CompileStatic
trait E1_CRM_Entity_T {
    @Getter
    static Object P1_is_identified_by_t = E41_Appellation_T.class
    @Getter
    static Object P2_has_type_t = E55_Type_T.class
    @Getter
    static Object AP12_has_level_of_description_t = E55_Type_T.class

    private ArrayList<E41_Appellation_T> P1_is_identified_by = new ArrayList<>()
    private ArrayList<E55_Type_T> P2_has_type = new ArrayList<>()
    private ArrayList<E55_Type_T> AP12_has_level_of_description = new ArrayList<>()

    Xsd_String P3_has_note

    static mapping = {
        P1_is_identified_by_t(edge: P1_is_identified_by_t)
        P2_has_type(edge: P2_has_type_t)
        AP12_has_level_of_description(edge: AP12_has_level_of_description_t)
    }
}