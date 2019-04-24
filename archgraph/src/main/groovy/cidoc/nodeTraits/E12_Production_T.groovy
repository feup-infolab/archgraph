package cidoc.nodeTraits

import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E12_Production_T implements E11_Modification_T, E63_Beginning_of_Existence_T{

    @Relationship(type="P108_has_produced")
    ArrayList<E24_Physical_ManMade_Thing_T> P108_has_produced = new ArrayList<>()

    ArrayList<E24_Physical_ManMade_Thing_T> getP108(){
        return P108_has_produced
    }

}
