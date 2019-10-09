package cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Edge
import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic
import lombok.Getter

@Vertex
@CompileStatic
trait E1_CRM_Entity_T {

    List<E55_Type_T> P2_has_type = new ArrayList<>()



    static mapping = {
        P2_has_type(edge: P2_has_type_E)
    }

}

@Edge(from = E1_CRM_Entity_T, to = E55_Type_T)
@CompileStatic
class P2_has_type_E {

}