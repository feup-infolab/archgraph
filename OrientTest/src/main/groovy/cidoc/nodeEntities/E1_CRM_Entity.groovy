package cidoc.nodeEntities

import cidoc.nodeTraits.E1_CRM_Entity_T
import cidoc.nodeTraits.E55_Type_T
import com.github.eugene.kamenev.orient.graph.Edge
import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic

@Vertex
@CompileStatic
class E1_CRM_Entity implements E1_CRM_Entity_T{

    public List<E55_Type_T> P2_has_type = new ArrayList<>()



    static mapping = {
        P2_has_type(edge: P2_has_type_E2)
    }
    Closure addToP2_has_type
}

@Edge(from = E1_CRM_Entity_T, to = E55_Type_T)
@CompileStatic
class P2_has_type_E2 {
    public Date since

}
