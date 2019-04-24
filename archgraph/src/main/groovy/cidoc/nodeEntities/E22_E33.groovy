package cidoc.nodeEntities

import cidoc.nodeTraits.E22_ManMade_Object_T
import cidoc.nodeTraits.E33_Linguistic_Object_T
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.NodeEntity

@CompileStatic
@NodeEntity
class E22_E33 extends Entity implements E22_ManMade_Object_T, E33_Linguistic_Object_T{

    
}
