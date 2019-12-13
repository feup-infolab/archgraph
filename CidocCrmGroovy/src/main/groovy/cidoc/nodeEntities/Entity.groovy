package cidoc.nodeEntities

import groovy.transform.CompileStatic;
import org.neo4j.ogm.annotation.GeneratedValue;
import org.neo4j.ogm.annotation.Id
import org.neo4j.ogm.annotation.NodeEntity;

@CompileStatic
@NodeEntity
abstract class Entity {
    @Id @GeneratedValue
    private Long id

    Long getId(){
        return id
    }

    Long setId(Long id){
        this.id = id
    }

    private String name

    String getName(){
        return name
    }

    void setName(String name) {
        this.name = name
    }
}
