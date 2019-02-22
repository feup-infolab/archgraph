package cidoc.nodeTraits


import org.neo4j.ogm.annotation.Relationship


trait E52_Time_Span_T implements E1_CRM_Entity_T{

    @Relationship(type = "P86_falls_within")
    private ArrayList<E52_Time_Span_T> P86_falls_within = new ArrayList<>()

    ArrayList<E52_Time_Span_T> getP86(){
        return P86_falls_within
    }

}