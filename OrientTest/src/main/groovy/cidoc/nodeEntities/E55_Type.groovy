package cidoc.nodeEntities

import cidoc.nodeTraits.E1_CRM_Entity_T
import cidoc.nodeTraits.E55_Type_T
import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic

@Vertex
@CompileStatic
class E55_Type implements E55_Type_T{

    List<E1_CRM_Entity_T> P2_is_type_of = new ArrayList<>()
}
