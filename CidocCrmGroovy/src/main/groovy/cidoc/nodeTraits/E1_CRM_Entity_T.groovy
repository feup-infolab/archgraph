package cidoc.nodeTraits


import org.neo4j.ogm.annotation.Relationship


trait E1_CRM_Entity_T {

    @Relationship(type="P1_is_identified_by")
    private ArrayList<E41_Appellation_T> P1_is_identified_by = new ArrayList<>()

    ArrayList<E41_Appellation_T> getP1(){
        return P1_is_identified_by;
    }



}