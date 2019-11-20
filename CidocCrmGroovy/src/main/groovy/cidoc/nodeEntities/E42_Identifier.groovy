package cidoc.nodeEntities

import cidoc.nodeTraits.E42_Identifier_T
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.NodeEntity

@CompileStatic
@NodeEntity
class E42_Identifier extends Entity implements E42_Identifier_T{
}
