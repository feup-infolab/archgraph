package cidoc.nodeEntities

import cidoc.nodeTraits.E22_ManMade_Object_T
import cidoc.nodeTraits.E38_Image_T
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.NodeEntity

@CompileStatic
@NodeEntity
class E22_E38 extends Entity implements E22_ManMade_Object_T, E38_Image_T{


}
