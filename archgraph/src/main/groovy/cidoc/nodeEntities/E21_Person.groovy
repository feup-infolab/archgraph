package cidoc.nodeEntities

import cidoc.nodeTraits.E21_Person_T
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.NodeEntity

@CompileStatic
@NodeEntity
class E21_Person extends Entity implements E21_Person_T{
}
