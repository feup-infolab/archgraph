package cidoc.nodeEntities

import cidoc.nodeTraits.E33_Linguistic_Object_T
import cidoc.nodeTraits.E84_Information_Carrier_T
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.NodeEntity

@CompileStatic
@NodeEntity
class E84_E33 extends Entity implements E84_Information_Carrier_T, E33_Linguistic_Object_T{


}
