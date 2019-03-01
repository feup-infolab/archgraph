package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait E24_Physical_ManMade_Thing_T implements E18_Physical_Thing_T,E71_Man_Made_Thing_T{

    @Relationship(type="P62_depicts")
    ArrayList<E1_CRM_Entity_T> P62_depicts = new ArrayList<>()

    ArrayList<E1_CRM_Entity_T> getP62(){
        return P62_depicts
    }



}