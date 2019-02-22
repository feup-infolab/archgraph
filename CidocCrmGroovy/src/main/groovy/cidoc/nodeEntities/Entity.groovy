package cidoc.nodeEntities;


import org.neo4j.ogm.annotation.GeneratedValue;
import org.neo4j.ogm.annotation.Id
import org.neo4j.ogm.annotation.NodeEntity;

@NodeEntity
abstract class Entity {
    @Id @GeneratedValue
    private Long id

    Long getId(){
        return id
    }

    private String name

    String getName(){
        return name
    }

    void setName(String name) {
        this.name = name
    }
}
