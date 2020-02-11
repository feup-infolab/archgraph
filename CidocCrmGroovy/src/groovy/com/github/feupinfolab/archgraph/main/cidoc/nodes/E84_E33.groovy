package cidoc.nodes

import cidoc.nodeTraits.E33_Linguistic_Object_T
import cidoc.nodeTraits.E84_Information_Carrier_T
import com.github.eugene.kamenev.orient.graph.Vertex
import groovy.transform.CompileStatic

@CompileStatic
@Vertex(initSchema = true)
class E84_E33 implements E84_Information_Carrier_T, E33_Linguistic_Object_T{


}
