package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait E53_Place_T {

    @Relationship(type="P87_is_identified_by")
    private ArrayList<E41_Appellation_T> P87_is_identified_by = new ArrayList<>()

    ArrayList<E41_Appellation_T> getP87(){
        return P87_is_identified_by
    }

}