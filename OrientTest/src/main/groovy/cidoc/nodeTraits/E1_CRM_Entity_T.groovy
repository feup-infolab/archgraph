package cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic
import lombok.Getter

@Vertex
@CompileStatic
trait E1_CRM_Entity_T {

    @Getter
    static Object P2_has_type_t = E55_Type_T.class

    private ArrayList<E55_Type_T> P2_has_type = new ArrayList<>()

    static mapping = {
        P2_has_type(edge: P2_has_type_t)
    }

}