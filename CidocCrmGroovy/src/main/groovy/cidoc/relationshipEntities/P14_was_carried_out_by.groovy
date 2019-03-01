package cidoc.relationshipEntities

import cidoc.nodeEntities.E55_Type
import cidoc.nodeTraits.E39_Actor_T
import cidoc.nodeTraits.E55_Type_T
import cidoc.nodeTraits.E7_Activity_T
import org.neo4j.ogm.annotation.EndNode
import org.neo4j.ogm.annotation.GeneratedValue
import org.neo4j.ogm.annotation.Id
import org.neo4j.ogm.annotation.RelationshipEntity
import org.neo4j.ogm.annotation.StartNode

@RelationshipEntity(type="P14_was_carried_out_by")
class P14_was_carried_out_by{

    @Id
    @GeneratedValue
    private Long id

    @StartNode E7_Activity_T e7_activity_t7

    @EndNode E39_Actor_T e39_actor_t

    E55_Type_T p14_1_in_the_role_of

    public P14_was_carried_out_by(E7_Activity_T e7, E39_Actor_T e39, E55_Type_T e55){
        this.e7_activity_t7 = e7
        this.e39_actor_t = e39
        this.p14_1_in_the_role_of = e55
    }

}
