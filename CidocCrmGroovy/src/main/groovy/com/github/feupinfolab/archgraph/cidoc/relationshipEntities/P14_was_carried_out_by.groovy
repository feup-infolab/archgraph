package com.github.feupinfolab.archgraph.cidoc.relationshipEntities

import com.github.feupinfolab.archgraph.cidoc.nodeTraits.E55_Type_T
import com.github.feupinfolab.archgraph.cidoc.nodes.E12_Production
import com.github.feupinfolab.archgraph.cidoc.nodes.E40_Legal_Body
import lombok.Getter
import lombok.Setter

import javax.persistence.GeneratedValue
import javax.persistence.Id

class P14_was_carried_out_by {
    @Id
    @GeneratedValue
    @Getter
    @Setter
    private Long id

    // @StartNode E12_Production e7_activity_t7

    // @EndNode E40_Legal_Body e39_actor_t

    E55_Type_T p14_1_in_the_role_of


    P14_was_carried_out_by(){}

    P14_was_carried_out_by(E12_Production e7, E40_Legal_Body e39, E55_Type_T e55){
        this.e7_activity_t7 = e7
        this.e39_actor_t = e39
        this.p14_1_in_the_role_of = e55
    }

}
