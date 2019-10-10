package cidoc.edges

import cidoc.nodeTraits.E1_CRM_Entity_T
import cidoc.nodeTraits.E41_Appellation_T
import com.github.eugene.kamenev.orient.graph.Edge
import groovy.transform.CompileStatic

@Edge(from = E1_CRM_Entity_T, to = E41_Appellation_T)
@CompileStatic
class P1_is_identified_by {

}
