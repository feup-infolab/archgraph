package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E74_Group_T implements E39_Actor_T{

    @Relationship(type="P107_has_current_or_former_member")
    private ArrayList<E39_Actor_T> P107_has_current_or_former_member = new ArrayList<>()


    ArrayList<E39_Actor_T> getP107() {
        return P107_has_current_or_former_member
    }


}