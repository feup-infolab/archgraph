package cidoc.nodeEntities

import groovy.transform.CompileStatic;
import com.github.eugene.kamenev.orient.graph.Vertex
import lombok.Getter
import lombok.Setter

import javax.persistence.GeneratedValue
import javax.persistence.Id

@CompileStatic
@Vertex
@Getter
@Setter
abstract class Entity {

}
