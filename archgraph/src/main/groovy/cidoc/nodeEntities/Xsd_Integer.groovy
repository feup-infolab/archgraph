package cidoc.nodeEntities

import org.neo4j.ogm.annotation.GeneratedValue
import org.neo4j.ogm.annotation.Id
import org.neo4j.ogm.annotation.NodeEntity

@NodeEntity
class Xsd_Integer {

    @Id @GeneratedValue
    private Long id

    Long getId(){
        return id
    }

    private int value

    int getValue(){
        return value
    }

    void setValue(int value) {
        this.value = value
    }

}
