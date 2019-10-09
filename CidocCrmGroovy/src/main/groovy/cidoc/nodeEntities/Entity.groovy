package cidoc.nodeEntities

import groovy.transform.CompileStatic;
import com.github.eugene.kamenev.orient.graph.Vertex
import javax.persistence.GeneratedValue
import javax.persistence.Id;

@CompileStatic
@Vertex
abstract class Entity {
    @Id
    @GeneratedValue
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
