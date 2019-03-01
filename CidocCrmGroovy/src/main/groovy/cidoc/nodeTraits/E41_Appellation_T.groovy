package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait E41_Appellation_T implements E90_Symbolic_Object_T{

    @Relationship(type="P139_has_alternative_form")
    private ArrayList<E41_Appellation_T> P139_has_alternative_form = new ArrayList<>()


    ArrayList<E41_Appellation_T> getP139() {
        return P139_has_alternative_form
    }

}