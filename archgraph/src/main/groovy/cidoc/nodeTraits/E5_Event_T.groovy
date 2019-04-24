package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E5_Event_T implements E4_Period_T{

    @Relationship(type="P11_had_participant")
    ArrayList<E39_Actor_T> P11_had_participant = new ArrayList<>()

    ArrayList<E39_Actor_T> getP11(){
        return P11_had_participant
    }

}