package cidoc.nodeTraits

import cidoc.nodeEntities.E1_Crm_Entity
import org.neo4j.ogm.annotation.Relationship

trait PC0_CRM_Property_T {

    @Relationship(type="P01_has_domain")
    private E1_CRM_Entity_T P01_has_domain

    E1_CRM_Entity_T getP01(){
        return P01_has_domain
    }

    void setP01(E1_CRM_Entity_T e1){
        P01_has_domain = e1

    }

    @Relationship(type="P02_has_range")
    private E1_CRM_Entity_T P02_has_range

    E1_CRM_Entity_T getP02(){
        return P02_has_range
    }

    void setP02(E1_CRM_Entity_T e1){
        P02_has_range = e1

    }

}