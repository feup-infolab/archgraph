package cidoc.nodeEntities

import org.neo4j.ogm.annotation.GeneratedValue
import org.neo4j.ogm.annotation.Id
import org.neo4j.ogm.annotation.NodeEntity

@NodeEntity
class Xsd_String extends Entity{
    @Id @GeneratedValue
    private Long id

    Long getId(){
        return id
    }

    private String value

    String getValue(){
        return value
    }

    void setValue(String value) {
        this.value = value
    }


}
