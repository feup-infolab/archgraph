package cidoc.nodeEntities

import cidoc.nodeTraits.E22_ManMade_Object_T
import cidoc.nodeTraits.E38_Image_T
import groovy.transform.CompileStatic
import com.github.eugene.kamenev.orient.graph.Vertex

@CompileStatic
@Vertex
class E22_E38 extends Entity implements E22_ManMade_Object_T, E38_Image_T{


}
