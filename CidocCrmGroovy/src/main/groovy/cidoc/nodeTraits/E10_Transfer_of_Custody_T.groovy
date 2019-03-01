package cidoc.nodeTraits

import org.neo4j.ogm.annotation.Relationship

trait E10_Transfer_of_Custody_T implements E7_Activity_T{

    @Relationship(type="P28_custody_surrendered_by")
    private ArrayList<E39_Actor_T> P28_custody_surrendered_by= new ArrayList<>()


    ArrayList<E39_Actor_T> getP28() {
        return P28_custody_surrendered_by
    }

    @Relationship(type="P29_custody_received_by")
    private ArrayList<E39_Actor_T> P29_custody_received_by= new ArrayList<>()


    ArrayList<E39_Actor_T> getP29() {
        return P29_custody_received_by
    }


    @Relationship(type="P30_transferred_custody_of")
    private ArrayList<E18_Physical_Thing_T> P30_transferred_custody_of= new ArrayList<>()


    ArrayList<E18_Physical_Thing_T> getP30() {
        return P30_transferred_custody_of
    }

}