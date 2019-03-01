package cidoc.nodeTraits


import org.neo4j.ogm.annotation.Relationship


trait E1_CRM_Entity_T {

    @Relationship(type="P1_is_identified_by")
    private ArrayList<E41_Appellation_T> P1_is_identified_by = new ArrayList<>()

    ArrayList<E41_Appellation_T> getP1(){
        return P1_is_identified_by
    }

    @Relationship(type="P2_has_type")
    private ArrayList<E55_Type_T> P2_has_type = new ArrayList<>()

    ArrayList<E55_Type_T> getP2(){
        return P2_has_type
    }




}