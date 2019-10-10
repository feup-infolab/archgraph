package cidoc.nodeTraits

import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic
import lombok.Getter
import lombok.Setter

@Vertex
@CompileStatic
trait E1_CRM_Entity_T {
    @Getter
    @Setter
    String name
}